function toggleModal(id) {
    document.getElementById(id).classList.toggle('is-active');
}

(function () {
    function applyOOBSwap(el) {
        var oob = el.getAttribute('hx-swap-oob');
        if (!oob) return;
        var clone = el.cloneNode(true);
        clone.removeAttribute('hx-swap-oob');
        if (oob === 'true' || oob === 'outerHTML') {
            var target = document.getElementById(el.id);
            if (target) {
                target.replaceWith(clone);
                if (typeof htmx !== 'undefined') htmx.process(clone);
            }
        } else if (oob.indexOf('afterbegin:') === 0) {
            var selector = oob.slice('afterbegin:'.length);
            var target2 = document.querySelector(selector);
            if (target2) {
                target2.insertAdjacentElement('afterbegin', clone);
                if (typeof htmx !== 'undefined') htmx.process(clone);
            }
        }
    }

    function connectWS() {
        var proto = location.protocol === 'https:' ? 'wss:' : 'ws:';
        var ws = new WebSocket(proto + '//' + location.host + '/ws');
        ws.onmessage = function (event) {
            var parser = new DOMParser();
            var doc = parser.parseFromString(event.data, 'text/html');
            Array.from(doc.body.children).forEach(applyOOBSwap);
        };
        ws.onclose = function () {
            setTimeout(connectWS, 3000);
        };
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', connectWS);
    } else {
        connectWS();
    }
}());
