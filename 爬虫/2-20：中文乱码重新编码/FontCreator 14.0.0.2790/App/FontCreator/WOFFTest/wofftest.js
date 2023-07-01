/*
  WebFont Demo javascript
  
  (C) 2013-2020 High-Logic B.V.
  
  http://www.high-logic.com
*/

var haveErrors = false;
var haveOTLF = false;

function Initialize() {
  if (fctrial) {
    AddError("This Web Font is created with a trial version of FontCreator. See the FontCreator User Manual about the limitations of exported fonts during the trial period.");
  }
  if (symbolfont) {
    AddError("Symbol fonts are legacy Windows fonts. They may not be supported by other operating systems, and word wrapping and spell check features won't work. Unicode fonts can contain symbols, so we recommend to convert your Symbol font to a Unicode font, unless you need to support old software. In FontCreator go to the main menu and select Tools -> Convert Font -> Convert to Unicode Font.");
  }
  BrowserCheck(otf.length > 0, colorfont);
  ProcessErrors();
  InitializeOpenTypeFeatures();
  InitializePreviewTextOptions();
  InitializeDirection();
  UpdatePreviewQuickPick(null);
  InitializeAxeSlidersAndInstances();
  InitializeMultipleInstancesPreview();
  InitializeVisabilityControler();
}


function AddError(aError) {
  haveErrors = true;
  id = document.getElementById('errorlist');
  id.innerHTML += "<li>" + aError + "</li>";
  return false;
}

function ProcessErrors() {
  if (!haveErrors) {
    document.getElementById('errors').style.display = "none";
  }
  else {
    document.getElementById("nojserror").style.display = "none";
  }
}

function DetermineBrowser() {
  var browserstr = navigator.userAgent.toLowerCase();
  var result = Array();
  result["name"] = "unknown";
  result["fullname"] = "unknown";
  result["version"] = "unknown";
  if (match = browserstr.match("edge/([0-9]+)")) {
    result["name"] = "edge";
    result["fullname"] = "Microsoft Edge";
    result["version"] = match[1];
  }
  else if (match = browserstr.match("chrome/([0-9]+)")) {
    result["name"] = "chrome";
    result["fullname"] = "Google Chrome";
    result["version"] = match[1];
  }
  else if (match = browserstr.match("firefox/([0-9]+)")) {
    result["name"] = "firefox";
    result["fullname"] = "Mozilla Firefox";
    result["version"] = match[1];
  }
  else if (match = browserstr.match("opera/([0-9]+)")) {
    result["name"] = "opera";
    result["fullname"] = "Opera";
    result["version"] = match[1];
  }
  else if (match = browserstr.match("safari/([0-9]+)")) {
    result["name"] = "safari";
    result["fullname"] = "Apple Safari";
    if (match = browserstr.match("version/([0-9\.]+)")) {
      result["version"] = match[1];
    }
  }
  else if (match = browserstr.match("msie ([0-9]+)")) {
    result["name"] = "ie";
    result["fullname"] = "Microsoft Internet Explorer";
    result["version"] = match[1];
  }
  else if (match = browserstr.match("trident/([0-9]+).+; .*? rv:([0-9]+)")) {
    /* IE 11 and up */
    if (match[1] >= 7) {
      result["name"] = "ie";
      result["fullname"] = "Microsoft Internet Explorer";
      result["version"] = match[2];
    }
  }
  return result;
}

function DetermineOS() {
  var browserstr = navigator.userAgent.toLowerCase();
  var result = Array();
  result["name"] = "unknown";
  result["version"] = "unknown";
  if (match = browserstr.match("windows.*? ([0-9\.]+);")) {
    result["name"] = "windows";
    result["version"] = match[1];
  }
  if (browserstr.indexOf("mac os x") > -1) {
    if (browserstr.indexOf("mobile") > -1) {
      result["name"] = "ios";
    } else {
      result["name"] = "osx";
    }
  }
  return result;
}

// converts HTML to text using Javascript
function html2text(html) {
  var temp = document.createElement("div");
  temp.innerHTML = html;
  return temp.textContent || temp.innerText || "";
}

function BrowserCheck(aOTLF, aColor) {

  var browser = DetermineBrowser();
  var os = DetermineOS();
  var id = document.getElementById("errorlist");

  //  return AddError(browser["name"] + " " + browser["version"] +" -> " + html2text(navigator.userAgent));

  switch (browser["name"]) {
    case "firefox":
      if (aOTLF) {
        if (browser["version"] < 4) {
          return AddError("You need at least FireFox 4 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
        }
      }
      if (aColor) {
        if (browser["version"] < 32) {
          return AddError("You need at least Firefox 32 in order to use color fonts.");
        }
      }
      break;
    case "chrome":
      if (browser["version"] < 22) {
        return AddError("You need at least Chrome 22 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
      }
      if (aColor) {
        if (browser["version"] < 71) {
          return AddError("You need at least Chrome 71 in order to use color fonts.");
        }
      }
      break;
    case "edge":
      // Should all work... 
      break;
    case "ie":
      if (aOTLF && (browser["version"] < 10)) {
        return AddError("You need at least Internet Explorer 10 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
      }
      if (aColor) {
        if (browser["version"] < 11) {
          return AddError("You need at least Internet Explorer 11 in order to use color fonts.");
        }
        else {
          if (os["version"] < 6.3) {
            return AddError("You need at least Windows 8.1 to use color fonts with Internet Explorer. Alternatively you can use Firefox which supports color fonts since version 32 on all platforms.");
          }
        }
      }
      break;
    case "opera":
      if (browser["version"] < 15) {
        return AddError("You need at least Opera 15 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
      }
      else {
        return AddWarning("Warning: This version of Opera might not support OpenType layout features.");
      }
      if (aColor) {
        return AddError("Opera does not support color fonts at least up to version 16.");
      }
      break;
    case "safari":
      if (os["name"] = "osx") {
        if (browser["version"] < 9.1) {
          return AddError("You need at least Safari 9.1 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
        }
      }
      if (os["name"] = "ios") {
        if (browser["version"] < 9.3) {
          return AddError("You need at least Mobile Safari 9.3 or a CSS 3.0 compatible browser in order to use OpenType layout features.");
        }
      }
      if (aColor) {
        if (browser["version"] < 11) {
          return AddError("You need at least Safari 11 in order to use color fonts.");
        }
      }
      break;
    default:
      return AddError("Unable to determine your browser and/or version. OpenType layout features might not display correctly.");
      break;
  }
}

function UpdateFeatures() {
  var featurestring = "";
  var part = "";

  altval = document.getElementById("alternate").value;

  for (i = 0; i < otf.length; i++) {
    options_element = document.getElementById("otf_" + otf[i][0]);
    selected_element = options_element.querySelector(".is-selected");
    selected_value = selected_element.value;

    part = "";
    if (selected_value != 0) {
      part = "'" + otf[i][0] + "' " + (selected_value == 1 ? altval : "0");
    }
    if (part != "") {
      if (featurestring != "") {
        featurestring += ",";
      }
      featurestring += part;
    }
  }
  id = document.getElementById("preview");
  // Firefox 4+
  id.style.MozFontFeatureSettings = featurestring;
  // Chrome 20+ / Safari (OSX only)
  id.style.webkitFontFeatureSettings = featurestring;
  // Official CSS 3.0
  id.style.fontFeatureSettings = featurestring;
}

function SetAllFeatures(value) {
  for (i = 0; i < otf.length; i++) {
    options_element = document.getElementById("otf_" + otf[i][0]);
    element_to_select = options_element.querySelector("[value='" + value + "']");
    MarkAsSelected(element_to_select);
  }
  UpdateFeatures();
}

function InitializeOpenTypeFeatures() {
  id = document.getElementById("otfeatures");
  if (otf.length == 0) {
    id.innerHTML += "This font does not contain any OpenType layout features.";
    return;

  }
  id.innerHTML += "<input type='button' value='Default' onclick='SetAllFeatures(0)'/> ";
  id.innerHTML += "<input type='button' value='Enable all' onclick='SetAllFeatures(1)'/> ";
  id.innerHTML += "<input type='button' value='Disable all' onclick='SetAllFeatures(2)'/><hr/>";
  for (i = 0; i < otf.length; i++) {
    id.innerHTML += "<div class='feature'><span class='feature-options' id='otf_" + otf[i][0] + "'><button onclick='MarkAsSelected(this);UpdateFeatures();' value='0' class='is-selected'>Default</button><button onclick='MarkAsSelected(this);UpdateFeatures();' value='1' class=''>On</button><button onclick='MarkAsSelected(this);UpdateFeatures();' value='2' class=''>Off</button></span> <label>" + otf[i][0] + " - " + otf[i][1] + "</label></div>";
  }
  UpdateFeatures();
}

function InitializePreviewTextOptions() {
  var newOptions = "";
  const previewtext_select = document.getElementById("previewtext");
  for (i = 0; i < previewtext.length; i++) {
    newOptions += '<option value="' + i + '">' + previewtext[i].substring(0, 140); + '</option>';
  }
  previewtext_select.innerHTML = newOptions;
}

function InitializeDirection() {
  id = document.getElementById("direction");
  if (initialdir === 'RTL') {
    id.value = 'rtl';
    UpdateDirection('rtl');
  } else {
    id.value = 'ltr';
    UpdateDirection('ltr');
  }
}

function UpdatePreviewText(sender) {
  id = document.getElementById("preview");
  id.innerHTML = sender.value.replace(/\n/g, "<br/>");

  id = document.getElementById("mi-preview");
  id.innerHTML = sender.value.replace(/\n/g, "<br/>");
}

function UpdatePreviewQuickPick(sender) {
  const input_element = document.getElementById("input");
  const value = document.getElementById('previewtext').value;
  input_element.value = previewtext[value];
  UpdatePreviewText(document.getElementById("input"));
}

function UpdateFontSize(sender) {
  id = document.getElementById("preview");
  id.style.fontSize = sender.value + "pt";
  id.style.lineHeight = sender.value + "pt";

  id = document.getElementById("mi-preview");
  id.style.fontSize = sender.value + "pt";
  id.style.lineHeight = sender.value + "pt";
}

function UpdateFontColorBG(sender) {
  id = document.getElementById("preview");
  id.style.background = "#" + sender.value;

  id = document.getElementById("mi-preview");
  id.style.background = "#" + sender.value;
}

function UpdateFontColorFG(sender) {
  id = document.getElementById("preview");
  id.style.color = "#" + sender.value;

  id = document.getElementById("mi-preview");
  id.style.color = "#" + sender.value;
}

function UpdateLanguage(sender) {
  id = document.getElementById("preview");
  id.lang = sender.value;

  id = document.getElementById("mi-preview");
  id.lang = sender.value;
}

function UpdateAlternate(sender) {
  UpdateFeatures();
}

function UpdateDirection(sender) {
  id = document.getElementById("preview");
  id.style.direction = sender.value;

  id = document.getElementById("mi-preview");
  id.style.direction = sender.value;
}

function MarkAsSelected(element) {
  element.parentElement.querySelector(".is-selected").classList.remove("is-selected");
  element.classList.add("is-selected");
}



/**
 * Axe Sliders
 * ---------
 * This is an anonymous function that runs only once with the axes variable, created in wofftest.html:
 * ---------
 * Code Examples for the "axes" var in the wofftest.html file:
 
    // If there are no axes:
    var axes = {}; 
 
    // One axe example (font FtConfetti):
    var axes = { 'wght': { name: 'Weight', value: 400, min: 100, max: 700 } }; 

    // Two axes example (font MutoatorSans):
    var axes = {
      'wght': {name: 'Weight', value: 400, min: 0, max: 1000},
      'wdth': {name: 'Width', value: 400, min: 0, max: 1000}
    };

    // Single line example with multiple axes:
    var axes = {'wght': {name: 'Weight', value: 0, min: 0, max: 1000}, 'wdth': {name: 'Width', value: 400, min: 0, max: 1000}, 'blah': {name: 'Blah', value: 725, min: 0, max: 1000}}; // Testing

 *
 */

function InitializeAxeSlidersAndInstances() {

  // SETTINGS:

  const duration = 7000;


  console.log('Initializing Axe Sliders for these axes:', axes);
  window.axesTags = Object.keys(axes); // returns ['wght', 'wdth']

  console.log('Initializing Instances for these instances:', instances);
  window.instancesArray = Object.keys(instances).map(key => ({ name: key, axes: Object.keys(instances[key]).map(axe => ({ name: axe, value: instances[key][axe] })) })) || []; // returns [{'name': 'SuperBold', axes: [{axe: 'wght', value: 300}]}]

  /////////////////

  console.log('Creating variables...');
  const play = '▶';
  const pause = '❚❚';

  /////////////////

  console.log('Finding #axessliders container in wofftest.html...');
  const $axesSlidersContainer = document.getElementById("axessliders");
  if (!$axesSlidersContainer) {
    console.error('#axessliders not found in wofftest.html. Please add it')
    return;
  } else {
    if (!axesTags.length) {
      $axesSlidersContainer.innerText = 'No axes found.';
      return;
    }
  }

  /////////////////

  console.log('Finding #instances container in wofftest.html...');
  const $instancesContainer = document.getElementById("instances");
  if (!$instancesContainer) {
    console.error('#instances not found in wofftest.html. Please add it')
    return;
  } else {
    if (!instancesArray.length) {
      $instancesContainer.innerText = 'No instances found.';
      return;
    }
  }

  /////////////////

  console.log('Adding HTML Axe to <fieldset id="axessliders"></fieldset>...');
  $axesSlidersContainer.innerHTML += `<legend>Axes</legend>`
  axesTags.forEach(axe => {
    $axesSlidersContainer.innerHTML += `
        <div class="axeslider" data-axe="${axe}" data-is-playing="false">
          <button name="playpause">${play}</button>
          <label title="${axe}">${axes[axe].name}:</label>
          <input type="range" value="${axes[axe].value}" step="${axes[axe].max <= 10 ? 0.1 : 1}" min="${axes[axe].min}" max="${axes[axe].max}">
          <input type="number" value="${axes[axe].value}" />
          <!--output>${axes[axe].value}</output-->
        </div>`;
  });

  /////////////////

  console.log('Adding HTML Instances to <fieldset id="instances"></fieldset>...');
  $instancesContainer.innerHTML += `<legend>Instances</legend>`
  instancesArray.forEach(instance => {
    $instancesContainer.innerHTML += `
        <div class="instance" data-instance="${instance.name}" data-is-current="false" title="${instance.axes.map(axe => `${axe.name}: ${axe.value}`).join(', ')}">
          <button>${instance.name}</button>
        </div>`;
  });



  /////////////////

  console.log('Setting up axe functions...');
  function updateAxesInPreview() {
    const $preview = document.getElementById("preview");
    let values = '';
    axesTags.forEach(axe => { values += `"${axe}" ${axes[axe].value},` });
    values = values.slice(0, -1); // removes last comma
    // console.log('Updates $preview Inline CSS to:', values);
    $preview.style.fontVariationSettings = values;
  }


  function updateAxeSliderValues(axe, value) {
    // console.log('Updating axe sliders values...');
    const $axeParent = document.querySelector(`[data-axe='${axe}']`);
    const $slider = $axeParent.querySelector('input[type=range]');
    const $output = $axeParent.querySelector('input[type=number]');
    $slider.value = value;
    $output.value = value;
  }

  function updateInstancesButtons() {

    const foundInstance = instancesArray.find(instance => {
      return axesTags.filter(axe => {
        // debugger;
        return instances[instance.name][axe] == axes[axe].value
      }).length === axesTags.length;
    });

    // Clear Old instances
    $instancesContainer.querySelectorAll('[data-is-current="true"]').forEach(selector => selector.setAttribute('data-is-current', 'false'));

    // Update Found instance
    if (foundInstance) {
      // console.log('foundInstance', foundInstance.name);
      $instancesContainer.querySelectorAll(`[data-instance="${foundInstance.name}"]`).forEach(selector => selector.setAttribute('data-is-current', 'true'));
    }

  }

  function updateAxeValueEverywhere(axe, value) {

    // console.log('Update axe value globally');
    axes[axe].value = parseInt(value);

    updateAxeSliderValues(axe, value);
    updateInstancesButtons();
    updateAxesInPreview();
  }

  /////////////////

  console.log('Initializing all axes functionallity...');
  axesTags.forEach(axe => {
    console.log(`%c axe: ${axe}... `, 'background: #bada55; color: black');

    /////////////////

    console.log('Finding all axe elements...');
    const $axeParent = $axesSlidersContainer.querySelector(`[data-axe='${axe}']`);
    const $axeButton = $axeParent.querySelector(`button[name='playpause']`);
    const $axeSlider = $axeParent.querySelector('input[type=range]');
    const $axeOutput = $axeParent.querySelector('input[type=number]');


    /////////////////

    console.log('Update Preview to the axes information...');
    updateInstancesButtons();
    updateAxesInPreview();

    /////////////////

    console.log('Adding Slider Listeners...');
    $axeSlider.addEventListener('input', () => {
      stopPlaying();
      updateAxeValueEverywhere(axe, $axeSlider.value);
      updateLeftovers();
    });
    $axeSlider.addEventListener('mouseup', () => {
      if (axes[axe].wasPlaying) {
        startPlaying();
        preStartPlaying();
      }
    });
    $axeOutput.addEventListener('input', () => {
      stopPlaying();
      updateAxeValueEverywhere(axe, $axeOutput.value);
      updateLeftovers();
    });

    // /////////////////

    // console.log('Moving forward...');
    axes[axe].move = 'forwards'; // forward/back
    axes[axe].leftovers = 0;

    /////////////////

    function setDecimalsBySteps(number) {
      const n = 1 / $axeSlider.getAttribute('step');
      return Math.round(number * n) / n;
    }

    console.log('Adding animation functions...');
    function loop() {
      // Loop this:

      const now = new Date();
      let ms = (now - axes[axe].since);
      ms = (axes[axe].moved === 'backwards') ? duration + ms : ms;

      const leftovers = axes[axe].moved === 'backwards' ? duration - axes[axe].leftovers : axes[axe].leftovers;
      ms = ms + leftovers;
      axes[axe].move = parseInt((ms) / duration % 2) ? 'backwards' : 'forwards';

      // document.getElementById('instances').querySelector('legend').innerText = axes[axe].move;

      if (axes[axe].move === 'forwards') {
        const calculatedValue = parseFloat(ms % duration / duration * (axes[axe].max - axes[axe].min)) + axes[axe].min;
        updateAxeValueEverywhere(axe, setDecimalsBySteps(calculatedValue));
      } else {
        const calculatedValue = (parseFloat(ms % duration / duration * (axes[axe].max - axes[axe].min)) * -1) + axes[axe].max;
        updateAxeValueEverywhere(axe, setDecimalsBySteps(calculatedValue));
      }

      // reset request, then play again
      axes[axe].request = undefined;
      startPlaying();
    }
    function startPlaying() {
      if (!axes[axe].request) {
        axes[axe].request = window.requestAnimationFrame(loop);
      }
    }
    function updateLeftovers() {
      axes[axe].leftovers = ($axeSlider.value - axes[axe].min) / (axes[axe].max - axes[axe].min) * duration;
    }
    function stopPlaying() {
      $axeParent.setAttribute('data-is-playing', 'false');
      $axeButton.innerHTML = play;
      if (axes[axe].request) {
        window.cancelAnimationFrame(axes[axe].request);
        axes[axe].since = new Date(); // now
        updateLeftovers();
        axes[axe].moved = axes[axe].move;
        axes[axe].request = undefined;
      }
    }

    /////////////////

    function preStartPlaying() {
      $axeParent.setAttribute('data-is-playing', 'true');
      $axeButton.innerHTML = pause;
    }

    console.log('Adding Playpause Listeners...');
    $axeButton.addEventListener('click', () => {
      const isPlaying = $axeParent.getAttribute('data-is-playing') === 'true';

      if (isPlaying) {
        // then Stop
        stopPlaying();
        axes[axe].wasPlaying = false;
        console.log(axe, 'stopped.');
      } else {
        // then Play
        preStartPlaying();
        startPlaying();
        axes[axe].wasPlaying = true;
        axes[axe].since = new Date();
        console.log(axe, 'playing...');
      }
    });

    /////////////////

    console.log(`%c axe: ${axe} DONE!`, 'background: #bada55; color: black');
  });


  console.log('Initializing all instancess functionallity...');
  instancesArray.forEach(instance => {
    console.log(`%c instances: ${JSON.stringify(instance)}... `, 'background: #bada55; color: black');

    /////////////////

    console.log('Finding Instance Elements for instance:', instance);
    const $instanceParent = $instancesContainer.querySelector(`[data-instance='${instance.name}']`);
    const $instanceButton = $instanceParent.querySelector(`button`);

    function forceStopPlayingAxe(axe) {
      const $axeParent = $axesSlidersContainer.querySelector(`[data-axe='${axe}'][data-is-playing="true"]`);
      if ($axeParent) {
        const $axeButton = $axeParent.querySelector(`button[name='playpause']`);
        $axeButton.click();
      }
    }

    /////////////////

    console.log('Adding Instance Button Listeners...');
    $instanceButton.addEventListener('click', () => {
      console.log('instance clicked');
      const instanceName = $instanceParent.getAttribute('data-instance');
      console.log('instanceName', instanceName);
      const _axes = instances[instanceName];
      console.log('_axes', _axes);
      Object.keys(_axes).map(axe => {
        updateAxeValueEverywhere(axe, _axes[axe]);
      });
      axesTags.map(axe => {
        forceStopPlayingAxe(axe);
        const $axeParent = $axesSlidersContainer.querySelector(`[data-axe='${axe}']`);
        const $axeSlider = $axeParent.querySelector('input[type=range]');
        axes[axe].leftovers = ($axeSlider.value - axes[axe].min) / (axes[axe].max - axes[axe].min) * duration;
      });

    });

    /////////////////

    console.log(`%c instance: ${instance} DONE!`, 'background: #bada55; color: black');
  });

};




function isOrContains(node, container) {
  while (node) {
    if (node === container) {
      return true;
    }
    node = node.parentNode;
  }
  return false;
}

function elementContainsSelection(el) {
  var sel;
  if (window.getSelection) {
    sel = window.getSelection();
    if (sel.rangeCount > 0) {
      for (var i = 0; i < sel.rangeCount; ++i) {
        if (!isOrContains(sel.getRangeAt(i).commonAncestorContainer, el)) {
          return false;
        }
      }
      return true;
    }
  } else if ((sel = document.selection) && sel.type != "Control") {
    return isOrContains(sel.createRange().parentElement(), el);
  }
  return false;
}


function InitializeMultipleInstancesPreview() {

  const $mi_container = document.getElementById("multiple-instances-preview");
  const $preview = document.getElementById("preview");
  const $mi_preview = $mi_container.querySelector("#mi-preview");
  const $possible_instances = $mi_container.querySelector("#possible_instances");
  const $clearBtn = $mi_container.querySelector("#clear");

  $possible_instances.innerHTML = instancesArray.map(instance => `<button data-instance-name="${instance.name}">${instance.name}</button>`).join(' ');

  $possible_instances.querySelectorAll('button').forEach($button => {
    $button.addEventListener('click', () => {

      // Abort everything if selection is not inside this
      if (!(elementContainsSelection($mi_preview) || elementContainsSelection($preview))) {
        console.log(`elementContainsSelection($preview)`, elementContainsSelection($preview));
        console.log(`elementContainsSelection($mi_preview)`, elementContainsSelection($mi_preview));
        alert('Please select some text from the previews first, then click on an instance.');
        return;
      }

      // Get instance data
      const instanceName = $button.getAttribute('data-instance-name');
      const axes = instances[instanceName];
      const values = axesTags.map(axe => `'${axe}' ${axes[axe]}`).join(', ');
      console.log('Updates $mi-preview Inline CSS to:', values);


      // Replace
      const selectedText = window.getSelection();
      const container = selectedText.anchorNode.parentNode;
      const wrappedText = `<span style="font-variation-settings:${values}">` + selectedText + '</span>'
      container.innerHTML = container.innerHTML.replace(selectedText, wrappedText);
    });
  });

  $clearBtn.addEventListener('click', () => {
    $preview.innerText = $preview.innerText.replace(/<[^>]*>?/gm, '');
    $mi_preview.innerText = $mi_preview.innerText.replace(/<[^>]*>?/gm, '');
  })
}


function InitializeVisabilityControler() {
  const $fieldsets = document.querySelectorAll('.has_visability_controller');
  $fieldsets.forEach($fieldset => {
    const $checkbox = $fieldset.querySelector('.visibility_controller');
    const $content = $fieldset.querySelector('.visibility_content');

    function check() {
      if ($checkbox.checked) {
        $fieldset.setAttribute('is-visible', 'true');
      } else {
        $fieldset.setAttribute('is-visible', 'false');
      }
    }

    $checkbox.addEventListener('change', check);
    check();
  });
}