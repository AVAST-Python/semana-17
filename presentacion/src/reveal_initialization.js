import Reveal from 'reveal.js';
import 'reveal.js/dist/reveal.css'

import './plugin/chalkboard/plugin.js'; // It's not a ES6 module
import './plugin/chalkboard/style.css'

import './plugin/customcontrols/plugin.js'; // It's not a ES6 module
import './plugin/customcontrols/style.css'

import './themes/sunblind_customized.css'

import RevealMath from 'reveal.js/plugin/math/math.esm.js';
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown.esm.js';
import RevealNotes from 'reveal.js/plugin/notes/notes.esm.js';
import RevealHighlight from 'reveal.js/plugin/highlight/highlight.esm.js';

// import 'reveal.js/plugin/highlight/monokai.css'
// import './plugin/highlight/styles/devibeans.css'
// import './plugin/highlight/styles/a11y-light.css'
import './plugin/highlight/styles/atom-one-light.css'
// import './plugin/highlight/styles/base16/atelier-dune-light.css'
// import './plugin/highlight/styles/base16/cupertino.css'
import './plugin/highlight/styles/base16/github.css'
// List of light themes:
// a11y-light
// atom-one-light
// base16-atelier-dune-light
// base16-atelier-forest.light
// base16-atelier-sulphurpool.light
// base16-cupertino
// base16-github

import RevealZoom from 'reveal.js/plugin/zoom/zoom.esm.js';

Reveal.initialize({
		width: 1280,
		height: 1050,
		controls: true,
		navigationMode: 'default',
		progress: true,
    history: true,
	  transition: 'fade', // possible values: 'linear', 'slide', 'zoom', 'concave', 'convex', 'fade'.
		transitionSpeed: 'slow', // default/fast/slow
		center: true,
		mouseWheel: false,
		previewLinks: false,
		slideNumber: true,
		animate: {
			autoplay: true
		},
		chalkboard: {
			storage: document.title,
			// theme: "blackbboard"
			theme: "whiteboard"
		},
		plugins: [
			RevealMarkdown,
			RevealMath,
			RevealChalkboard,
      RevealCustomControls,
      RevealHighlight,
      RevealNotes, // S to open notes
      RevealZoom
    ],
    keyboard: {
      65: function() { RevealChalkboard.toggleNotesCanvas() }, // Annotate when 'a' is pressed
      66: function() { RevealChalkboard.toggleChalkboard() },	 // Toggle board when 'b' is pressed
      46: function() { RevealChalkboard.clear() },	// clear chalkboard when 'DEL' is pressed
      8: function() { RevealChalkboard.reset() },	// reset chalkboard data on current slide with 'BACKSPACE'
      68: function() { RevealChalkboard.download() },	// download recorded chalkboard drawing when 'd' is pressed
      88: function() { RevealChalkboard.colorNext() }, // cycle colors forward when 'x' is pressed
      90: function() { RevealChalkboard.colorPrev() }, // cycle colors backward when 'z' is pressed
			// For the remote control
			37: 'prev', 38: 'prev',
			39: 'next', 40: 'next',
	  },
    customcontrols: {
			controls: [
				{ icon: '<i class="fa fa-pen-square"></i>',
			  	title: 'Toggle chalkboard (B)',
			  	action: 'RevealChalkboard.toggleChalkboard();'
				},
				{ icon: '<i class="fa fa-pen"></i>',
			  	title: 'Toggle notes canvas (C)',
			  	action: 'RevealChalkboard.toggleNotesCanvas();'
				}
			]
		},
	})
