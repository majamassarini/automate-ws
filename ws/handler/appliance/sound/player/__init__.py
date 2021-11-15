import home
from ws.handler.appliance.light.indoor.dimmerable import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.Appliance
    LABEL_FADE_IN = "Fade In"
    LABEL_FADE_OUT = "Fade Out"
    ICON_FADE_IN = "fas fa-volume-up"
    ICON_FADE_OUT = "fas fa-volume-off"
    ICON_FORCED_ON = "fas fa-play-circle"
    ICON_OFF = "far fa-play-circle"

    def get_label(self, appliance):
        if appliance.state.VALUE == home.appliance.sound.player.state.off.State.VALUE:
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_in.State.VALUE
        ):
            return self.LABEL_FADE_IN
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_out.State.VALUE
        ):
            return self.LABEL_FADE_OUT
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.LABEL_FORCED_CIRCADIAN_RHYTHM

    def get_icon(self, appliance):
        if appliance.state.VALUE == home.appliance.sound.player.state.off.State.VALUE:
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_in.State.VALUE
        ):
            return self.ICON_FADE_IN
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_out.State.VALUE
        ):
            return self.ICON_FADE_OUT
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.ICON_FORCED_CIRCADIAN_RHYTHM

    def is_displayed(self, appliance, event):
        result = False
        if isinstance(
            event,
            (
                home.appliance.sound.player.event.sleepy_volume.Event,
                home.event.presence.Event,
                home.event.sleepiness.Event,
                appliance.forced_enum,
            ),
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.on.State.VALUE
            or appliance.state.VALUE
            == home.appliance.sound.player.state.off.State.VALUE
        ) and (
            isinstance(
                event,
                (
                    home.appliance.sound.player.event.volume.Event,
                    home.appliance.sound.player.event.playlist.Event,
                ),
            )
            and not isinstance(
                event,
                (
                    home.appliance.sound.player.event.fade_in.volume.Event,
                    home.appliance.sound.player.event.fade_in.playlist.Event,
                    home.appliance.sound.player.event.fade_out.volume.Event,
                    home.appliance.sound.player.event.fade_out.playlist.Event,
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event,
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event,
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event,
                ),
            )
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.forced.circadian_rhythm.State.VALUE
            and (
                isinstance(
                    event,
                    (
                        home.event.user.Event,
                        home.appliance.sound.player.event.volume.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event,
                    ),
                )
                and not isinstance(
                    event,
                    (
                        home.appliance.sound.player.event.fade_in.volume.Event,
                        home.appliance.sound.player.event.fade_in.playlist.Event,
                        home.appliance.sound.player.event.fade_out.volume.Event,
                        home.appliance.sound.player.event.fade_out.playlist.Event,
                        home.appliance.sound.player.event.playlist.Event,
                    ),
                )
            )
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_in.State.VALUE
            and (
                isinstance(
                    event,
                    (
                        home.appliance.sound.player.event.fade_in.volume.Event,
                        home.appliance.sound.player.event.fade_in.playlist.Event,
                        home.event.elapsed.Event,
                    ),
                )
                and not isinstance(
                    event,
                    (
                        home.appliance.sound.player.event.fade_out.volume.Event,
                        home.appliance.sound.player.event.fade_out.playlist.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event,
                    ),
                )
            )
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.sound.player.state.fade_in.State.VALUE
            and (
                isinstance(
                    event,
                    (
                        home.appliance.sound.player.event.fade_out.volume.Event,
                        home.appliance.sound.player.event.fade_out.playlist.Event,
                        home.event.elapsed.Event,
                    ),
                )
                and not isinstance(
                    event,
                    (
                        home.appliance.sound.player.event.fade_in.volume.Event,
                        home.appliance.sound.player.event.fade_in.playlist.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event,
                        home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event,
                    ),
                )
            )
        ):
            result = True
        return result
