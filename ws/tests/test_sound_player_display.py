"""Each sound player volume scale is shown, and editable, only in the state
that plays it: volume_scale in Sleepy Forced On, fade_in.volume_scale in Fade
In, fade_out.volume_scale in Fade Out."""

import unittest
from types import SimpleNamespace

import home
from ws.handler import event_mapper
from ws.handler.appliance.sound.player import Handler

event = home.appliance.sound.player.event
state = home.appliance.sound.player.state

SCALES = {
    state.forced.sleepy_on.State.VALUE: event.volume_scale.Event(75),
    state.fade_in.State.VALUE: event.fade_in.volume_scale.Event(20),
    state.fade_out.State.VALUE: event.fade_out.volume_scale.Event(45),
}


def _appliance(value):
    return SimpleNamespace(
        state=SimpleNamespace(VALUE=value), forced_enum=event.forced.Event
    )


class TestSoundPlayerVolumeScaleDisplay(unittest.TestCase):
    def setUp(self):
        self.handler = Handler(None)

    def test_each_scale_has_an_event_handler(self):
        for scale in SCALES.values():
            self.assertIn((None, type(scale)), event_mapper)

    def test_each_state_shows_only_its_own_scale(self):
        for value in SCALES:
            appliance = _appliance(value)
            for owner, scale in SCALES.items():
                self.assertEqual(
                    self.handler.is_displayed(appliance, scale),
                    owner == value,
                    f"{type(scale).__module__} in {value}",
                )

    def test_other_states_show_no_scale(self):
        for value in (
            state.off.State.VALUE,
            state.forced.on.State.VALUE,
            state.forced.off.State.VALUE,
            state.forced.circadian_rhythm.State.VALUE,
        ):
            for scale in SCALES.values():
                self.assertFalse(
                    self.handler.is_displayed(_appliance(value), scale)
                )

    def test_fade_out_shows_its_volume_and_playlist(self):
        appliance = _appliance(state.fade_out.State.VALUE)
        self.assertTrue(
            self.handler.is_displayed(appliance, event.fade_out.volume.Event(20))
        )
        self.assertTrue(
            self.handler.is_displayed(
                appliance, event.fade_out.playlist.Event("Fade out")
            )
        )
        self.assertFalse(
            self.handler.is_displayed(appliance, event.fade_in.volume.Event(30))
        )


if __name__ == "__main__":
    unittest.main()
