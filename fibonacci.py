<!DOCTYPE html>
<!-- saved from url=(0027)https://www.onlinegdb.com/# -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><script type="text/javascript" async="" src="./fibonacci_files/publishertag.prebid.123.js.download"></script><script type="text/javascript" async="" src="./fibonacci_files/localstore.js.download"></script><script type="text/javascript" src="./fibonacci_files/shares.json"></script><script type="text/javascript" src="./fibonacci_files/shares(1).json"></script><style id="ace-idle-fingers">.ace-idle-fingers .ace_gutter {
  background: #3b3b3b;
  color: rgb(153,153,153)
}

.ace-idle-fingers .ace_print-margin {
  width: 1px;
  background: #3b3b3b
}

.ace-idle-fingers {
  background-color: #323232;
  color: #FFFFFF
}

.ace-idle-fingers .ace_cursor {
  color: #91FF00
}

.ace-idle-fingers .ace_marker-layer .ace_selection {
  background: rgba(90, 100, 126, 0.88)
}

.ace-idle-fingers.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #323232;
}

.ace-idle-fingers .ace_marker-layer .ace_step {
  background: rgb(102, 82, 0)
}

.ace-idle-fingers .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid #404040
}

.ace-idle-fingers .ace_marker-layer .ace_active-line {
  background: #353637
}

.ace-idle-fingers .ace_gutter-active-line {
  background-color: #353637
}

.ace-idle-fingers .ace_marker-layer .ace_selected-word {
  border: 1px solid rgba(90, 100, 126, 0.88)
}

.ace-idle-fingers .ace_invisible {
  color: #404040
}

.ace-idle-fingers .ace_keyword,
.ace-idle-fingers .ace_meta {
  color: #CC7833
}

.ace-idle-fingers .ace_constant,
.ace-idle-fingers .ace_constant.ace_character,
.ace-idle-fingers .ace_constant.ace_character.ace_escape,
.ace-idle-fingers .ace_constant.ace_other,
.ace-idle-fingers .ace_support.ace_constant {
  color: #6C99BB
}

.ace-idle-fingers .ace_invalid {
  color: #FFFFFF;
  background-color: #FF0000
}

.ace-idle-fingers .ace_fold {
  background-color: #CC7833;
  border-color: #FFFFFF
}

.ace-idle-fingers .ace_support.ace_function {
  color: #B83426
}

.ace-idle-fingers .ace_variable.ace_parameter {
  font-style: italic
}

.ace-idle-fingers .ace_string {
  color: #A5C261
}

.ace-idle-fingers .ace_string.ace_regexp {
  color: #CCCC33
}

.ace-idle-fingers .ace_comment {
  font-style: italic;
  color: #BC9458
}

.ace-idle-fingers .ace_meta.ace_tag {
  color: #FFE5BB
}

.ace-idle-fingers .ace_entity.ace_name {
  color: #FFC66D
}

.ace-idle-fingers .ace_collab.ace_user1 {
  color: #323232;
  background-color: #FFF980
}

.ace-idle-fingers .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWMwMjLyZYiPj/8PAAreAwAI1+g0AAAAAElFTkSuQmCC) right repeat-y
}

.ace-idle-fingers .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
}

/*# sourceURL=ace/css/ace-idle-fingers */</style><script type="text/javascript" src="./fibonacci_files/1.txt"></script><script type="text/javascript" src="./fibonacci_files/1(1).txt"></script><style id="autocompletion.css">
.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {
    background-color: #CAD6FA;
    z-index: 1;
}
.ace_dark.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {
    background-color: #3a674e;
}
.ace_editor.ace_autocomplete .ace_line-hover {
    border: 1px solid #abbffe;
    margin-top: -1px;
    background: rgba(233,233,253,0.4);
    position: absolute;
    z-index: 2;
}
.ace_dark.ace_editor.ace_autocomplete .ace_line-hover {
    border: 1px solid rgba(109, 150, 13, 0.8);
    background: rgba(58, 103, 78, 0.62);
}
.ace_completion-meta {
    opacity: 0.5;
    margin: 0.9em;
}
.ace_completion-message {
    color: blue;
}
.ace_editor.ace_autocomplete .ace_completion-highlight{
    color: #2d69c7;
}
.ace_dark.ace_editor.ace_autocomplete .ace_completion-highlight{
    color: #93ca12;
}
.ace_editor.ace_autocomplete {
    width: 300px;
    z-index: 200000;
    border: 1px lightgray solid;
    position: fixed;
    box-shadow: 2px 3px 5px rgba(0,0,0,.2);
    line-height: 1.4;
    background: #fefefe;
    color: #111;
}
.ace_dark.ace_editor.ace_autocomplete {
    border: 1px #484747 solid;
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.51);
    line-height: 1.4;
    background: #25282c;
    color: #c1c1c1;
}
/*# sourceURL=ace/css/autocompletion.css */</style><style id="snippets.css">
.ace_snippet-marker {
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    background: rgba(194, 193, 208, 0.09);
    border: 1px dotted rgba(211, 208, 235, 0.62);
    position: absolute;
}
/*# sourceURL=ace/css/snippets.css */</style><style id="error_marker.css">
    .error_widget_wrapper {
        background: inherit;
        color: inherit;
        border:none
    }
    .error_widget {
        border-top: solid 2px;
        border-bottom: solid 2px;
        margin: 5px 0;
        padding: 10px 40px;
        white-space: pre-wrap;
    }
    .error_widget.ace_error, .error_widget_arrow.ace_error{
        border-color: #ff5a5a
    }
    .error_widget.ace_warning, .error_widget_arrow.ace_warning{
        border-color: #F1D817
    }
    .error_widget.ace_info, .error_widget_arrow.ace_info{
        border-color: #5a5a5a
    }
    .error_widget.ace_ok, .error_widget_arrow.ace_ok{
        border-color: #5aaa5a
    }
    .error_widget_arrow {
        position: absolute;
        border: solid 5px;
        border-top-color: transparent!important;
        border-right-color: transparent!important;
        border-left-color: transparent!important;
        top: -5px;
    }

/*# sourceURL=ace/css/error_marker.css */</style><style id="ace-tm">.ace-tm .ace_gutter {
  background: #f0f0f0;
  color: #333;
}

.ace-tm .ace_print-margin {
  width: 1px;
  background: #e8e8e8;
}

.ace-tm .ace_fold {
    background-color: #6B72E6;
}

.ace-tm {
  background-color: #FFFFFF;
  color: black;
}

.ace-tm .ace_cursor {
  color: black;
}
        
.ace-tm .ace_invisible {
  color: rgb(191, 191, 191);
}

.ace-tm .ace_storage,
.ace-tm .ace_keyword {
  color: blue;
}

.ace-tm .ace_constant {
  color: rgb(197, 6, 11);
}

.ace-tm .ace_constant.ace_buildin {
  color: rgb(88, 72, 246);
}

.ace-tm .ace_constant.ace_language {
  color: rgb(88, 92, 246);
}

.ace-tm .ace_constant.ace_library {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_invalid {
  background-color: rgba(255, 0, 0, 0.1);
  color: red;
}

.ace-tm .ace_support.ace_function {
  color: rgb(60, 76, 114);
}

.ace-tm .ace_support.ace_constant {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_support.ace_type,
.ace-tm .ace_support.ace_class {
  color: rgb(109, 121, 222);
}

.ace-tm .ace_keyword.ace_operator {
  color: rgb(104, 118, 135);
}

.ace-tm .ace_string {
  color: rgb(3, 106, 7);
}

.ace-tm .ace_comment {
  color: rgb(76, 136, 107);
}

.ace-tm .ace_comment.ace_doc {
  color: rgb(0, 102, 255);
}

.ace-tm .ace_comment.ace_doc.ace_tag {
  color: rgb(128, 159, 191);
}

.ace-tm .ace_constant.ace_numeric {
  color: rgb(0, 0, 205);
}

.ace-tm .ace_variable {
  color: rgb(49, 132, 149);
}

.ace-tm .ace_xml-pe {
  color: rgb(104, 104, 91);
}

.ace-tm .ace_entity.ace_name.ace_function {
  color: #0000A2;
}


.ace-tm .ace_heading {
  color: rgb(12, 7, 255);
}

.ace-tm .ace_list {
  color:rgb(185, 6, 144);
}

.ace-tm .ace_meta.ace_tag {
  color:rgb(0, 22, 142);
}

.ace-tm .ace_string.ace_regex {
  color: rgb(255, 0, 0)
}

.ace-tm .ace_marker-layer .ace_selection {
  background: rgb(181, 213, 255);
}
.ace-tm.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px white;
}
.ace-tm .ace_marker-layer .ace_step {
  background: rgb(252, 255, 0);
}

.ace-tm .ace_marker-layer .ace_stack {
  background: rgb(164, 229, 101);
}

.ace-tm .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgb(192, 192, 192);
}

.ace-tm .ace_marker-layer .ace_active-line {
  background: rgba(0, 0, 0, 0.07);
}

.ace-tm .ace_gutter-active-line {
    background-color : #dcdcdc;
}

.ace-tm .ace_marker-layer .ace_selected-word {
  background: rgb(250, 250, 255);
  border: 1px solid rgb(200, 200, 250);
}

.ace-tm .ace_indent-guide {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
}

.ace-tm .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
}

/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">/*
styles = []
for (var i = 1; i < 16; i++) {
    styles.push(".ace_br" + i + "{" + (
        ["top-left", "top-right", "bottom-right", "bottom-left"]
    ).map(function(x, j) {
        return i & (1<<j) ? "border-" + x + "-radius: 3px;" : "" 
    }).filter(Boolean).join(" ") + "}")
}
styles.join("\n")
*/
.ace_br1 {border-top-left-radius    : 3px;}
.ace_br2 {border-top-right-radius   : 3px;}
.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}
.ace_br4 {border-bottom-right-radius: 3px;}
.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}
.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}
.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}
.ace_br8 {border-bottom-left-radius : 3px;}
.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}
.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}
.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}
.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}


.ace_editor {
    position: relative;
    overflow: hidden;
    padding: 0;
    font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;
    direction: ltr;
    text-align: left;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.ace_scroller {
    position: absolute;
    overflow: hidden;
    top: 0;
    bottom: 0;
    background-color: inherit;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    cursor: text;
}

.ace_content {
    position: absolute;
    box-sizing: border-box;
    min-width: 100%;
    contain: style size layout;
    font-variant-ligatures: no-common-ligatures;
}

.ace_dragging .ace_scroller:before{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    content: '';
    background: rgba(250, 250, 250, 0.01);
    z-index: 1000;
}
.ace_dragging.ace_dark .ace_scroller:before{
    background: rgba(0, 0, 0, 0.01);
}

.ace_gutter {
    position: absolute;
    overflow : hidden;
    width: auto;
    top: 0;
    bottom: 0;
    left: 0;
    cursor: default;
    z-index: 4;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    contain: style size layout;
}

.ace_gutter-active-line {
    position: absolute;
    left: 0;
    right: 0;
}

.ace_scroller.ace_scroll-left {
    box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;
}

.ace_gutter-cell {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    padding-left: 19px;
    padding-right: 6px;
    background-repeat: no-repeat;
}

.ace_gutter-cell.ace_error {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: 2px center;
}

.ace_gutter-cell.ace_warning {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");
    background-position: 2px center;
}

.ace_gutter-cell.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");
    background-position: 2px center;
}
.ace_dark .ace_gutter-cell.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");
}

.ace_scrollbar {
    contain: strict;
    position: absolute;
    right: 0;
    bottom: 0;
    z-index: 6;
}

.ace_scrollbar-inner {
    position: absolute;
    cursor: text;
    left: 0;
    top: 0;
}

.ace_scrollbar-v{
    overflow-x: hidden;
    overflow-y: scroll;
    top: 0;
}

.ace_scrollbar-h {
    overflow-x: scroll;
    overflow-y: hidden;
    left: 0;
}

.ace_print-margin {
    position: absolute;
    height: 100%;
}

.ace_text-input {
    position: absolute;
    z-index: 0;
    width: 0.5em;
    height: 1em;
    opacity: 0;
    background: transparent;
    -moz-appearance: none;
    appearance: none;
    border: none;
    resize: none;
    outline: none;
    overflow: hidden;
    font: inherit;
    padding: 0 1px;
    margin: 0 -1px;
    contain: strict;
    -ms-user-select: text;
    -moz-user-select: text;
    -webkit-user-select: text;
    user-select: text;
    /*with `pre-line` chrome inserts &nbsp; instead of space*/
    white-space: pre!important;
}
.ace_text-input.ace_composition {
    background: transparent;
    color: inherit;
    z-index: 1000;
    opacity: 1;
}
.ace_composition_placeholder { color: transparent }
.ace_composition_marker { 
    border-bottom: 1px solid;
    position: absolute;
    border-radius: 0;
    margin-top: 1px;
}

[ace_nocontext=true] {
    transform: none!important;
    filter: none!important;
    clip-path: none!important;
    mask : none!important;
    contain: none!important;
    perspective: none!important;
    mix-blend-mode: initial!important;
    z-index: auto;
}

.ace_layer {
    z-index: 1;
    position: absolute;
    overflow: hidden;
    /* workaround for chrome bug https://github.com/ajaxorg/ace/issues/2312*/
    word-wrap: normal;
    white-space: pre;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    /* setting pointer-events: auto; on node under the mouse, which changes
        during scroll, will break mouse wheel scrolling in Safari */
    pointer-events: none;
}

.ace_gutter-layer {
    position: relative;
    width: auto;
    text-align: right;
    pointer-events: auto;
    height: 1000000px;
    contain: style size layout;
}

.ace_text-layer {
    font: inherit !important;
    position: absolute;
    height: 1000000px;
    width: 1000000px;
    contain: style size layout;
}

.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {
    contain: style size layout;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

.ace_hidpi .ace_text-layer,
.ace_hidpi .ace_gutter-layer,
.ace_hidpi .ace_content,
.ace_hidpi .ace_gutter {
    contain: strict;
    will-change: transform;
}
.ace_hidpi .ace_text-layer > .ace_line, 
.ace_hidpi .ace_text-layer > .ace_line_group {
    contain: strict;
}

.ace_cjk {
    display: inline-block;
    text-align: center;
}

.ace_cursor-layer {
    z-index: 4;
}

.ace_cursor {
    z-index: 4;
    position: absolute;
    box-sizing: border-box;
    border-left: 2px solid;
    /* workaround for smooth cursor repaintng whole screen in chrome */
    transform: translatez(0);
}

.ace_multiselect .ace_cursor {
    border-left-width: 1px;
}

.ace_slim-cursors .ace_cursor {
    border-left-width: 1px;
}

.ace_overwrite-cursors .ace_cursor {
    border-left-width: 0;
    border-bottom: 1px solid;
}

.ace_hidden-cursors .ace_cursor {
    opacity: 0.2;
}

.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {
    opacity: 0;
}

.ace_smooth-blinking .ace_cursor {
    transition: opacity 0.18s;
}

.ace_animate-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: step-end;
    animation-name: blink-ace-animate;
    animation-iteration-count: infinite;
}

.ace_animate-blinking.ace_smooth-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: ease-in-out;
    animation-name: blink-ace-animate-smooth;
}
    
@keyframes blink-ace-animate {
    from, to { opacity: 1; }
    60% { opacity: 0; }
}

@keyframes blink-ace-animate-smooth {
    from, to { opacity: 1; }
    45% { opacity: 1; }
    60% { opacity: 0; }
    85% { opacity: 0; }
}

.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {
    position: absolute;
    z-index: 3;
}

.ace_marker-layer .ace_selection {
    position: absolute;
    z-index: 5;
}

.ace_marker-layer .ace_bracket {
    position: absolute;
    z-index: 6;
}

.ace_marker-layer .ace_error_bracket {
    position: absolute;
    border-bottom: 1px solid #DE5555;
    border-radius: 0;
}

.ace_marker-layer .ace_active-line {
    position: absolute;
    z-index: 2;
}

.ace_marker-layer .ace_selected-word {
    position: absolute;
    z-index: 4;
    box-sizing: border-box;
}

.ace_line .ace_fold {
    box-sizing: border-box;

    display: inline-block;
    height: 11px;
    margin-top: -2px;
    vertical-align: middle;

    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");
    background-repeat: no-repeat, repeat-x;
    background-position: center center, top left;
    color: transparent;

    border: 1px solid black;
    border-radius: 2px;

    cursor: pointer;
    pointer-events: auto;
}

.ace_dark .ace_fold {
}

.ace_fold:hover{
    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");
}

.ace_tooltip {
    background-color: #FFF;
    background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));
    border: 1px solid gray;
    border-radius: 1px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    color: black;
    max-width: 100%;
    padding: 3px 4px;
    position: fixed;
    z-index: 999999;
    box-sizing: border-box;
    cursor: default;
    white-space: pre;
    word-wrap: break-word;
    line-height: normal;
    font-style: normal;
    font-weight: normal;
    letter-spacing: normal;
    pointer-events: none;
}

.ace_folding-enabled > .ace_gutter-cell {
    padding-right: 13px;
}

.ace_fold-widget {
    box-sizing: border-box;

    margin: 0 -12px 0 1px;
    display: none;
    width: 11px;
    vertical-align: top;

    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: center;

    border-radius: 3px;
    
    border: 1px solid transparent;
    cursor: pointer;
}

.ace_folding-enabled .ace_fold-widget {
    display: inline-block;   
}

.ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");
}

.ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");
}

.ace_fold-widget:hover {
    border: 1px solid rgba(0, 0, 0, 0.3);
    background-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
}

.ace_fold-widget:active {
    border: 1px solid rgba(0, 0, 0, 0.4);
    background-color: rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
}
/**
 * Dark version for fold widgets
 */
.ace_dark .ace_fold-widget {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");
}
.ace_dark .ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget:hover {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
    background-color: rgba(255, 255, 255, 0.1);
}
.ace_dark .ace_fold-widget:active {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
}

.ace_inline_button {
    border: 1px solid lightgray;
    display: inline-block;
    margin: -1px 8px;
    padding: 0 5px;
    pointer-events: auto;
    cursor: pointer;
}
.ace_inline_button:hover {
    border-color: gray;
    background: rgba(200,200,200,0.2);
    display: inline-block;
    pointer-events: auto;
}

.ace_fold-widget.ace_invalid {
    background-color: #FFB4B4;
    border-color: #DE5555;
}

.ace_fade-fold-widgets .ace_fold-widget {
    transition: opacity 0.4s ease 0.05s;
    opacity: 0;
}

.ace_fade-fold-widgets:hover .ace_fold-widget {
    transition: opacity 0.05s ease 0.05s;
    opacity:1;
}

.ace_underline {
    text-decoration: underline;
}

.ace_bold {
    font-weight: bold;
}

.ace_nobold .ace_bold {
    font-weight: normal;
}

.ace_italic {
    font-style: italic;
}


.ace_error-marker {
    background-color: rgba(255, 0, 0,0.2);
    position: absolute;
    z-index: 9;
}

.ace_highlight-marker {
    background-color: rgba(255, 255, 0,0.2);
    position: absolute;
    z-index: 8;
}

.ace_mobile-menu {
    position: absolute;
    line-height: 1.5;
    border-radius: 4px;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    background: white;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #dcdcdc;
    color: black;
}
.ace_dark > .ace_mobile-menu {
    background: #333;
    color: #ccc;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #444;

}
.ace_mobile-button {
    padding: 2px;
    cursor: pointer;
    overflow: hidden;
}
.ace_mobile-button:hover {
    background-color: #eee;
    opacity:1;
}
.ace_mobile-button:active {
    background-color: #ddd;
}

.ace_placeholder {
    font-family: arial;
    transform: scale(0.9);
    transform-origin: left;
    white-space: pre;
    opacity: 0.7;
    margin: 0 10px;
}
/*# sourceURL=ace/css/ace_editor.css */</style><script type="text/javascript" src="./fibonacci_files/moatframe.js.download"></script>
    <title> GDB online Debugger | Compiler - Code, Compile, Run, Debug online C, C++</title>

    
    <meta name="description" content="Online GDB is online compiler and debugger for C/C++. You can compile, run and debug code with gdb online. Using gcc/g++ as compiler and gdb as debugger. Currently C and C++ languages are supported.">
    <meta name="keywords" content="gdb online, online gdb, online debugger, debugger online, online compiler, debug c online, debug c program online, debug c code online, debug c++ program online, debug c++ code online, debug c++ online, online gdb debugger">
<meta name="google-site-verification" content="LRk_5wLIzc43hz9wV6QksHTiqYHM1CoAbHZVzigvn9s">
<meta name="verify-admitad" content="fb09364f2b">
    <meta property="og:title" content="">
    <meta property="og:site_name" content="GDB online Debugger">
    <meta property="og:description" content="Online GDB is online compiler and debugger for C/C++. You can compile, run and debug code with gdb online. Using gcc/g++ as compiler and gdb as debugger. Currently C and C++ languages are supported.">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="icon" href="https://www.onlinegdb.com/favicon.ico" type="image/x-icon">
    <!--<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.6/dist/css/bootstrap.min.css">-->
    <!--<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha512-nNo+yCHEyn0smMxSswnf/OnX6/KwJuZTlNZBjauKhTK0c+zT+q5JOCx0UFhXQ6rJR9jg6Es8gPuD2uZcYDLqSw==" crossorigin="anonymous" referrerpolicy="no-referrer" />-->
    <link rel="stylesheet" href="./fibonacci_files/bootstrap.min.css">

    
    <link rel="stylesheet" href="./fibonacci_files/onlinegdb.css">
    
    
    <script type="text/javascript" async="" src="./fibonacci_files/analytics.js.download"></script><script type="text/javascript" async="" src="./fibonacci_files/js"></script><script>  var main_ide =  true;  </script>
    
    
    <script type="text/javascript" src="./fibonacci_files/onlinegdb.js.download"></script><style type="text/css">  .JColResizer{table-layout:fixed;} .JColResizer > tbody > tr > td, .JColResizer > tbody > tr > th{overflow:hidden}  .JPadding > tbody > tr > td, .JPadding > tbody > tr > th{/*padding-left:0!important; */padding-right:0!important;} .JCLRgrips{ height:0px; position:relative;} .JCLRgrip{margin-left:-5px; position:absolute; z-index:5; } .JCLRgrip .JColResizer{position:absolute;background-color:red;filter:alpha(opacity=1);opacity:0;width:10px;height:100%;cursor: col-resize;top:0px} .JCLRLastGrip{position:absolute; width:1px; } .JCLRgripDrag{ border-left:1px dotted black;	} .JCLRFlex{width:auto!important;} .JCLRgrip.JCLRdisabledGrip .JColResizer{cursor:default; display:none;}</style>
    <script type="text/javascript" src="./fibonacci_files/ace.js.download"></script>
    <script type="text/javascript" src="./fibonacci_files/ext-language_tools.js.download"></script>
    <script type="text/javascript" src="./fibonacci_files/editor.js.download" defer=""></script>
    <script type="text/javascript" src="./fibonacci_files/main.js.download" defer=""></script>
    

    <link rel="stylesheet" href="./fibonacci_files/bootstrap-select.min.css">
    <script src="./fibonacci_files/bootstrap-select.min.js.download"></script>

    




    
    
    <!--<script src="/public/js/bsa.js?v=4"></script>-->
    <script type="text/javascript">(function(){var bsa_optimize=document.createElement('script');bsa_optimize.type='text/javascript';bsa_optimize.async=true;bsa_optimize.src='https://cdn-s2s.buysellads.net/pub/onlinegdb.js?'+(new Date()-new Date()%3600000);(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa_optimize);})();</script><script type="text/javascript" async="" src="./fibonacci_files/onlinegdb.js(1).download"></script>
    <script type="text/javascript" src="./fibonacci_files/monetization.js.download"></script>
    

    
<style type="text/css">
            html, body {
                height: 100%;
                min-height: 100%;
                margin: 0;
                padding: 0;
            }
            .split-pane-divider{
                background: #aaa;
            }
            
            #left-component {
                width: 20%;
/*                min-width: 20vw;
                max-width: 20vw;*/
                background-color: #337ab7;
            }
            #right-left-component {
                width: 100%;
                background-color: #f5f5f5;
            }
            #right-right-component {
                left: 100%;
                margin-left:1px;
                /*min-width: 15em;*/
                background-color: #f5f5f5;
            }
            #top-component {
                height: 75%;
                position: relative;
                background-color: #f5f5f5;
            }
            #my-divider {
                left: 20%; /* Same as left component width */
                width: 2px;
            }
            #my-divider1 {
				top: 75%;
				height: 7px;
                background-color:#bdbdbd;
			}
            #my-divider2 {
                left: 100%; /* Same as left component width */
                width: 1px;
            }
            #bottom-component {
                background-color: #f5f5f5;
                top:75%;
                margin-top: 1px;
            }
            #right-component {
                background-color: #f5f5f5;
/*                max-width:80vw;
                min-width:80vw;
                min-width:17em;*/
                
                left: 20%;  /* Same as left component width */
                
                /*margin-left: 2px;  /* Same as divider width */
            }
            @media only screen and (max-width: 760px) {
                #mobile_test_element { display: none; }
            }
        </style>
        
<div id="_bsa_srv-CK7I6K7M_0"></div><style type="text/css">.at-icon{fill:#fff;border:0}.at-icon-wrapper{display:inline-block;overflow:hidden}a .at-icon-wrapper{cursor:pointer}.at-rounded,.at-rounded-element .at-icon-wrapper{border-radius:12%}.at-circular,.at-circular-element .at-icon-wrapper{border-radius:50%}.addthis_32x32_style .at-icon{width:2pc;height:2pc}.addthis_24x24_style .at-icon{width:24px;height:24px}.addthis_20x20_style .at-icon{width:20px;height:20px}.addthis_16x16_style .at-icon{width:1pc;height:1pc}#at16lb{display:none;position:absolute;top:0;left:0;width:100%;height:100%;z-index:1001;background-color:#000;opacity:.001}#at_complete,#at_error,#at_share,#at_success{position:static!important}.at15dn{display:none}#at15s,#at16p,#at16p form input,#at16p label,#at16p textarea,#at_share .at_item{font-family:arial,helvetica,tahoma,verdana,sans-serif!important;font-size:9pt!important;outline-style:none;outline-width:0;line-height:1em}* html #at15s.mmborder{position:absolute!important}#at15s.mmborder{position:fixed!important;width:250px!important}#at15s{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);float:none;line-height:1em;margin:0;overflow:visible;padding:5px;text-align:left;position:absolute}#at15s a,#at15s span{outline:0;direction:ltr;text-transform:none}#at15s .at-label{margin-left:5px}#at15s .at-icon-wrapper{width:1pc;height:1pc;vertical-align:middle}#at15s .at-icon{width:1pc;height:1pc}.at4-icon{display:inline-block;background-repeat:no-repeat;background-position:top left;margin:0;overflow:hidden;cursor:pointer}.addthis_16x16_style .at4-icon,.addthis_default_style .at4-icon,.at4-icon,.at-16x16{width:1pc;height:1pc;line-height:1pc;background-size:1pc!important}.addthis_32x32_style .at4-icon,.at-32x32{width:2pc;height:2pc;line-height:2pc;background-size:2pc!important}.addthis_24x24_style .at4-icon,.at-24x24{width:24px;height:24px;line-height:24px;background-size:24px!important}.addthis_20x20_style .at4-icon,.at-20x20{width:20px;height:20px;line-height:20px;background-size:20px!important}.at4-icon.circular,.circular .at4-icon,.circular.aticon{border-radius:50%}.at4-icon.rounded,.rounded .at4-icon{border-radius:4px}.at4-icon-left{float:left}#at15s .at4-icon{text-indent:20px;padding:0;overflow:visible;white-space:nowrap;background-size:1pc;width:1pc;height:1pc;background-position:top left;display:inline-block;line-height:1pc}.addthis_vertical_style .at4-icon,.at4-follow-container .at4-icon{margin-right:5px}html>body #at15s{width:250px!important}#at15s.atm{background:none!important;padding:0!important;width:10pc!important}#at15s_inner{background:#fff;border:1px solid #fff;margin:0}#at15s_head{position:relative;background:#f2f2f2;padding:4px;cursor:default;border-bottom:1px solid #e5e5e5}.at15s_head_success{background:#cafd99!important;border-bottom:1px solid #a9d582!important}.at15s_head_success a,.at15s_head_success span{color:#000!important;text-decoration:none}#at15s_brand,#at15sptx,#at16_brand{position:absolute}#at15s_brand{top:4px;right:4px}.at15s_brandx{right:20px!important}a#at15sptx{top:4px;right:4px;text-decoration:none;color:#4c4c4c;font-weight:700}#at15sptx:hover{text-decoration:underline}#at16_brand{top:5px;right:30px;cursor:default}#at_hover{padding:4px}#at_hover .at_item,#at_share .at_item{background:#fff!important;float:left!important;color:#4c4c4c!important}#at_share .at_item .at-icon-wrapper{margin-right:5px}#at_hover .at_bold{font-weight:700;color:#000!important}#at_hover .at_item{width:7pc!important;padding:2px 3px!important;margin:1px;text-decoration:none!important}#at_hover .at_item.athov,#at_hover .at_item:focus,#at_hover .at_item:hover{margin:0!important}#at_hover .at_item.athov,#at_hover .at_item:focus,#at_hover .at_item:hover,#at_share .at_item.athov,#at_share .at_item:hover{background:#f2f2f2!important;border:1px solid #e5e5e5;color:#000!important;text-decoration:none}.ipad #at_hover .at_item:focus{background:#fff!important;border:1px solid #fff}.at15t{display:block!important;height:1pc!important;line-height:1pc!important;padding-left:20px!important;background-position:0 0;text-align:left}.addthis_button,.at15t{cursor:pointer}.addthis_toolbox a.at300b,.addthis_toolbox a.at300m{width:auto}.addthis_toolbox a{margin-bottom:5px;line-height:initial}.addthis_toolbox.addthis_vertical_style{width:200px}.addthis_button_facebook_like .fb_iframe_widget{line-height:100%}.addthis_button_facebook_like iframe.fb_iframe_widget_lift{max-width:none}.addthis_toolbox a.addthis_button_counter,.addthis_toolbox a.addthis_button_facebook_like,.addthis_toolbox a.addthis_button_facebook_send,.addthis_toolbox a.addthis_button_facebook_share,.addthis_toolbox a.addthis_button_foursquare,.addthis_toolbox a.addthis_button_linkedin_counter,.addthis_toolbox a.addthis_button_pinterest_pinit,.addthis_toolbox a.addthis_button_tweet{display:inline-block}.addthis_toolbox span.addthis_follow_label{display:none}.addthis_toolbox.addthis_vertical_style span.addthis_follow_label{display:block;white-space:nowrap}.addthis_toolbox.addthis_vertical_style a{display:block}.addthis_toolbox.addthis_vertical_style.addthis_32x32_style a{line-height:2pc;height:2pc}.addthis_toolbox.addthis_vertical_style .at300bs{margin-right:4px;float:left}.addthis_toolbox.addthis_20x20_style span{line-height:20px}.addthis_toolbox.addthis_32x32_style span{line-height:2pc}.addthis_toolbox.addthis_pill_combo_style .addthis_button_compact .at15t_compact,.addthis_toolbox.addthis_pill_combo_style a{float:left}.addthis_toolbox.addthis_pill_combo_style a.addthis_button_tweet{margin-top:-2px}.addthis_toolbox.addthis_pill_combo_style .addthis_button_compact .at15t_compact{margin-right:4px}.addthis_default_style .addthis_separator{margin:0 5px;display:inline}div.atclear{clear:both}.addthis_default_style .addthis_separator,.addthis_default_style .at4-icon,.addthis_default_style .at300b,.addthis_default_style .at300bo,.addthis_default_style .at300bs,.addthis_default_style .at300m{float:left}.at300b img,.at300bo img{border:0}a.at300b .at4-icon,a.at300m .at4-icon{display:block}.addthis_default_style .at300b,.addthis_default_style .at300bo,.addthis_default_style .at300m{padding:0 2px}.at300b,.at300bo,.at300bs,.at300m{cursor:pointer}.addthis_button_facebook_like.at300b:hover,.addthis_button_facebook_like.at300bs:hover,.addthis_button_facebook_send.at300b:hover,.addthis_button_facebook_send.at300bs:hover{opacity:1}.addthis_20x20_style .at15t,.addthis_20x20_style .at300bs{overflow:hidden;display:block;height:20px!important;width:20px!important;line-height:20px!important}.addthis_32x32_style .at15t,.addthis_32x32_style .at300bs{overflow:hidden;display:block;height:2pc!important;width:2pc!important;line-height:2pc!important}.at300bs{overflow:hidden;display:block;background-position:0 0;height:1pc;width:1pc;line-height:1pc!important}.addthis_default_style .at15t_compact,.addthis_default_style .at15t_expanded{margin-right:4px}#at_share .at_item{width:123px!important;padding:4px;margin-right:2px;border:1px solid #fff}#at16p{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);z-index:10000001;position:absolute;top:50%;left:50%;width:300px;padding:10px;margin:0 auto;margin-top:-185px;margin-left:-155px;font-family:arial,helvetica,tahoma,verdana,sans-serif;font-size:9pt;color:#5e5e5e}#at_share{margin:0;padding:0}#at16pt{position:relative;background:#f2f2f2;height:13px;padding:5px 10px}#at16pt a,#at16pt h4{font-weight:700}#at16pt h4{display:inline;margin:0;padding:0;font-size:9pt;color:#4c4c4c;cursor:default}#at16pt a{position:absolute;top:5px;right:10px;color:#4c4c4c;text-decoration:none;padding:2px}#at15sptx:focus,#at16pt a:focus{outline:thin dotted}#at15s #at16pf a{top:1px}#_atssh{width:1px!important;height:1px!important;border:0!important}.atm{width:10pc!important;padding:0;margin:0;line-height:9pt;letter-spacing:normal;font-family:arial,helvetica,tahoma,verdana,sans-serif;font-size:9pt;color:#444;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);padding:4px}.atm-f{text-align:right;border-top:1px solid #ddd;padding:5px 8px}.atm-i{background:#fff;border:1px solid #d5d6d6;padding:0;margin:0;box-shadow:1px 1px 5px rgba(0,0,0,.15)}.atm-s{margin:0!important;padding:0!important}.atm-s a:focus{border:transparent;outline:0;transition:none}#at_hover.atm-s a,.atm-s a{display:block;text-decoration:none;padding:4px 10px;color:#235dab!important;font-weight:400;font-style:normal;transition:none}#at_hover.atm-s .at_bold{color:#235dab!important}#at_hover.atm-s a:hover,.atm-s a:hover{background:#2095f0;text-decoration:none;color:#fff!important}#at_hover.atm-s .at_bold{font-weight:700}#at_hover.atm-s a:hover .at_bold{color:#fff!important}.atm-s a .at-label{vertical-align:middle;margin-left:5px;direction:ltr}.at_PinItButton{display:block;width:40px;height:20px;padding:0;margin:0;background-image:url(//s7.addthis.com/static/t00/pinit00.png);background-repeat:no-repeat}.at_PinItButton:hover{background-position:0 -20px}.addthis_toolbox .addthis_button_pinterest_pinit{position:relative}.at-share-tbx-element .fb_iframe_widget span{vertical-align:baseline!important}#at16pf{height:auto;text-align:right;padding:4px 8px}.at-privacy-info{position:absolute;left:7px;bottom:7px;cursor:pointer;text-decoration:none;font-family:helvetica,arial,sans-serif;font-size:10px;line-height:9pt;letter-spacing:.2px;color:#666}.at-privacy-info:hover{color:#000}.body .wsb-social-share .wsb-social-share-button-vert{padding-top:0;padding-bottom:0}.body .wsb-social-share.addthis_counter_style .addthis_button_tweet.wsb-social-share-button{padding-top:40px}.body .wsb-social-share.addthis_counter_style .addthis_button_facebook_like.wsb-social-share-button{padding-top:21px}@media print{#at4-follow,#at4-share,#at4-thankyou,#at4-whatsnext,#at4m-mobile,#at15s,.at4,.at4-recommended{display:none!important}}@media screen and (max-width:400px){.at4win{width:100%}}@media screen and (max-height:700px) and (max-width:400px){.at4-thankyou-inner .at4-recommended-container{height:122px;overflow:hidden}.at4-thankyou-inner .at4-recommended .at4-recommended-item:first-child{border-bottom:1px solid #c5c5c5}}</style><style type="text/css">.at-branding-logo{font-family:helvetica,arial,sans-serif;text-decoration:none;font-size:10px;display:inline-block;margin:2px 0;letter-spacing:.2px}.at-branding-logo .at-branding-icon{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAMAAAC67D+PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////+GlNUkcc1QAAAB1JREFUeNpiYIQDBjQmAwMmkwEM0JnY1WIxFyDAABGeAFEudiZsAAAAAElFTkSuQmCC")}.at-branding-logo .at-branding-icon,.at-branding-logo .at-privacy-icon{display:inline-block;height:10px;width:10px;margin-left:4px;margin-right:3px;margin-bottom:-1px;background-repeat:no-repeat}.at-branding-logo .at-privacy-icon{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKCAMAAABR24SMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRF8fr9ot/xXcfn2/P5AKva////////AKTWodjhjAAAAAd0Uk5T////////ABpLA0YAAAA6SURBVHjaJMzBDQAwCAJAQaj7b9xifV0kUKJ9ciWxlzWEWI5gMF65KUTv0VKkjVeTerqE/x7+9BVgAEXbAWI8QDcfAAAAAElFTkSuQmCC")}.at-branding-logo span{text-decoration:none}.at-branding-logo .at-branding-addthis,.at-branding-logo .at-branding-powered-by{color:#666}.at-branding-logo .at-branding-addthis:hover{color:#333}.at-cv-with-image .at-branding-addthis,.at-cv-with-image .at-branding-addthis:hover{color:#fff}a.at-branding-logo:visited{color:initial}.at-branding-info{display:inline-block;padding:0 5px;color:#666;border:1px solid #666;border-radius:50%;font-size:10px;line-height:9pt;opacity:.7;transition:all .3s ease;text-decoration:none}.at-branding-info span{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.at-branding-info:before{content:'i';font-family:Times New Roman}.at-branding-info:hover{color:#0780df;border-color:#0780df}</style><script src="./fibonacci_files/theme-idle_fingers.js.download"></script><script src="./fibonacci_files/mode-c_cpp.js.download"></script><script type="text/javascript" charset="utf-8" async="" src="./fibonacci_files/layers.fa6cd1947ce26e890d3d.js.download"></script><script src="./fibonacci_files/c_cpp.js.download"></script><script id="_carbonads_projs" type="text/javascript" src="./fibonacci_files/CKYI5KJI.json"></script><style type="text/css">.at-share-dock.atss{top:auto;left:0;right:0;bottom:0;width:100%;max-width:100%;z-index:1000200;box-shadow:0 0 1px 1px #e2dfe2}.at-share-dock.at-share-dock-zindex-hide{z-index:-1!important}.at-share-dock.atss-top{bottom:auto;top:0}.at-share-dock a{width:auto;transition:none;color:#fff;text-decoration:none;box-sizing:content-box;-webkit-box-sizing:content-box;-moz-box-sizing:content-box}.at-share-dock a:hover{width:auto}.at-share-dock .at4-count{height:43px;padding:5px 0 0;line-height:20px;background:#fff;font-family:Helvetica neue,arial}.at-share-dock .at4-count span{width:100%}.at-share-dock .at4-count .at4-share-label{color:#848484;font-size:10px;letter-spacing:1px}.at-share-dock .at4-count .at4-counter{top:2px;position:relative;display:block;color:#222;font-size:22px}.at-share-dock.at-shfs-medium .at4-count{height:36px;line-height:1pc;padding-top:4px}.at-share-dock.at-shfs-medium .at4-count .at4-counter{font-size:18px}.at-share-dock.at-shfs-medium .at-share-btn .at-icon-wrapper,.at-share-dock.at-shfs-medium a .at-icon-wrapper{padding:6px 0}.at-share-dock.at-shfs-small .at4-count{height:26px;line-height:1;padding-top:3px}.at-share-dock.at-shfs-small .at4-count .at4-share-label{font-size:8px}.at-share-dock.at-shfs-small .at4-count .at4-counter{font-size:14px}.at-share-dock.at-shfs-small .at-share-btn .at-icon-wrapper,.at-share-dock.at-shfs-small a .at-icon-wrapper{padding:4px 0}</style><style type="text/css">div.at-share-close-control.ats-dark,div.at-share-open-control-left.ats-dark,div.at-share-open-control-right.ats-dark{background:#262b30}div.at-share-close-control.ats-light,div.at-share-open-control-left.ats-light,div.at-share-open-control-right.ats-light{background:#fff}div.at-share-close-control.ats-gray,div.at-share-open-control-left.ats-gray,div.at-share-open-control-right.ats-gray{background:#f2f2f2}.atss{position:fixed;top:20%;width:3pc;z-index:100020;background:none}.at-share-close-control{position:relative;width:3pc;overflow:auto}.at-share-open-control-left{position:fixed;top:20%;z-index:100020;left:0;width:22px}.at-share-close-control .at4-arrow.at-left{float:right}.atss-left{left:0;float:left;right:auto}.atss-right{left:auto;float:right;right:0}.atss-right.at-share-close-control .at4-arrow.at-right{position:relative;right:0;overflow:auto}.atss-right.at-share-close-control .at4-arrow{float:left}.at-share-open-control-right{position:fixed;top:20%;z-index:100020;right:0;width:22px;float:right}.atss-right .at-share-close-control .at4-arrow{float:left}.atss.atss-right a{float:right}.atss.atss-right .at4-share-title{float:right;overflow:hidden}.atss .at-share-btn,.atss a{position:relative;display:block;width:3pc;margin:0;outline-offset:-1px;text-align:center;float:left;transition:width .15s ease-in-out;overflow:hidden;background:#e8e8e8;z-index:100030;cursor:pointer}.at-share-btn::-moz-focus-inner{border:0;padding:0}.atss-right .at-share-btn{float:right}.atss .at-share-btn{border:0;padding:0}.atss .at-share-btn:focus,.atss .at-share-btn:hover,.atss a:focus,.atss a:hover{width:4pc}.atss .at-share-btn .at-icon-wrapper,.atss a .at-icon-wrapper{display:block;padding:8px 0}.atss .at-share-btn:last-child,.atss a:last-child{border:none}.atss .at-share-btn span .at-icon,.atss a span .at-icon{position:relative;top:0;left:0;display:block;background-repeat:no-repeat;background-position:50% 50%;width:2pc;height:2pc;line-height:2pc;border:none;padding:0;margin:0 auto;overflow:hidden;cursor:pointer;cursor:hand}.at4-share .at-custom-sidebar-counter{font-family:Helvetica neue,arial;vertical-align:top;margin-right:4px;display:inline-block;text-align:center}.at4-share .at-custom-sidebar-count{font-size:17px;line-height:1.25em;color:#222}.at4-share .at-custom-sidebar-text{font-size:9px;line-height:1.25em;color:#888;letter-spacing:1px}.at4-share .at4-share-count-container{position:absolute;left:0;right:auto;top:auto;bottom:0;width:100%;color:#fff;background:inherit}.at4-share .at4-share-count,.at4-share .at4-share-count-container{line-height:1pc;font-size:10px}.at4-share .at4-share-count{text-indent:0;font-family:Arial,Helvetica Neue,Helvetica,sans-serif;font-weight:200;width:100%;height:1pc}.at4-share .at4-share-count-anchor{padding-bottom:8px;text-decoration:none;transition:padding .15s ease-in-out .15s,width .15s ease-in-out}</style><style type="text/css">#at4-drawer-outer-container{top:0;width:20pc;position:fixed}#at4-drawer-outer-container.at4-drawer-inline{position:relative}#at4-drawer-outer-container.at4-drawer-inline.at4-drawer-right{float:right;right:0;left:auto}#at4-drawer-outer-container.at4-drawer-inline.at4-drawer-left{float:left;left:0;right:auto}#at4-drawer-outer-container.at4-drawer-shown,#at4-drawer-outer-container.at4-drawer-shown *{z-index:999999}#at4-drawer-outer-container,#at4-drawer-outer-container .at4-drawer-outer,#at-drawer{height:100%;overflow-y:auto;overflow-x:hidden}.at4-drawer-push-content-right-back{position:relative;right:0}.at4-drawer-push-content-right{position:relative;left:20pc!important}.at4-drawer-push-content-left-back{position:relative;left:0}.at4-drawer-push-content-left{position:relative;right:20pc!important}#at4-drawer-outer-container.at4-drawer-right{left:auto;right:-20pc}#at4-drawer-outer-container.at4-drawer-left{right:auto;left:-20pc}#at4-drawer-outer-container.at4-drawer-shown.at4-drawer-right{left:auto;right:0}#at4-drawer-outer-container.at4-drawer-shown.at4-drawer-left{right:auto;left:0}#at-drawer{top:0;z-index:9999999;height:100%;animation-duration:.4s}#at-drawer.drawer-push.at-right{right:-20pc}#at-drawer.drawer-push.at-left{left:-20pc}#at-drawer .at-recommended-label{padding:0 0 0 20px;color:#999;line-height:3pc;font-size:18px;font-weight:300;cursor:default}#at-drawer-arrow{width:30px;height:5pc}#at-drawer-arrow.ats-dark{background:#262b30}#at-drawer-arrow.ats-gray{background:#f2f2f2}#at-drawer-open-arrow{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAABcCAYAAAC1OT8uAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjk3ODNCQjdERUQ3QjExRTM5NjFGRUZBODc3MTIwMTNCIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjk3ODNCQjdFRUQ3QjExRTM5NjFGRUZBODc3MTIwMTNCIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6OTc4M0JCN0JFRDdCMTFFMzk2MUZFRkE4NzcxMjAxM0IiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6OTc4M0JCN0NFRDdCMTFFMzk2MUZFRkE4NzcxMjAxM0IiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7kstzCAAAB4ElEQVR42uyWv0oDQRDGb9dYimgVjliID2Ca9AGfwtZob2Grja1PIFj7EhGCYK99VPBPOkVMp8X5rc6FeN7dfjOksMjAxwXZ3667OzvfLKRr682l5ZV9aDh+fxsnRHhoDzqGLjFBi4XOoFtoAxowoB893o/w7WpAl/+QgQMBwwRdTPhUC2lAV/wDA7qy5WOgq9psHejqTqkKdLE7KYCv0JZjMgBgB58raBG6mP1K6j2pT099T+qMUOeeOss1wDcEIA1PnQXy576rAUI0oFMoC7VCnn40Gs8Pd4lAiXNUKmJ0lh1mPzGEWiyUCqAGW3Pwv4IvUJsFO9CHgP3Zr6Te0xwgAf3LxaAjS241pbikCRkOg+nSJdV4p8HOPl3vvRYI5dtrgVDvvcWovcWovcWovcWovcWovcWovQChWNywNpqvdAKtQp/QNmPUIQ6kwwqt2Xmsxf6GMPM1Pptsbz45CPmXqKb+15Gz4J/LZcDSNIqBlQlbB0afe1mmUDWiCNKFZRq0VKMeXY1CTDq2sJLWsCmoaBBRqNRR6qBKC6qCaj2rDIqaXBGiXHEaom00h1S+K3fVlr6HNuqgvgCh0+owt21bybQn8+mZ78mcEebcM2e5+T2ZX24ZqCph0qn1vgQYAJ/KDpLQr2tPAAAAAElFTkSuQmCC);background-repeat:no-repeat;width:13px;height:23px;margin:28px 0 0 8px}.at-left #at-drawer-open-arrow{background-position:0 -46px}.ats-dark #at-drawer-open-arrow{background-position:0 -23px}.ats-dark.at-left #at-drawer-open-arrow{background-position:0 -69px}#at-drawer-arrow.at4-drawer-modern-browsers{position:fixed;top:40%;background-repeat:no-repeat;background-position:0 0!important;z-index:9999999}.at4-drawer-inline #at-drawer-arrow{position:absolute}#at-drawer-arrow.at4-drawer-modern-browsers.at-right{right:0}#at-drawer-arrow.at4-drawer-modern-browsers.at-left{left:0}.at4-drawer-push-animation-left{transition:left .4s ease-in-out .15s}.at4-drawer-push-animation-right{transition:right .4s ease-in-out .15s}#at-drawer.drawer-push.at4-drawer-push-animation-right{right:0}#at-drawer.drawer-push.at4-drawer-push-animation-right-back{right:-20pc!important}#at-drawer.drawer-push.at4-drawer-push-animation-left{left:0}#at-drawer.drawer-push.at4-drawer-push-animation-left-back{left:-20pc!important}#at-drawer .at4-closebutton.drawer-close{content:'X';color:#999;display:block;position:absolute;margin:0;top:0;right:0;width:3pc;height:45px;line-height:45px;overflow:hidden;opacity:.5}#at-drawer.ats-dark .at4-closebutton.drawer-close{color:#fff}#at-drawer .at4-closebutton.drawer-close:hover{opacity:1}#at-drawer.ats-dark.at4-recommended .at4-logo-container a{color:#666}#at-drawer.at4-recommended .at4-recommended-vertical{padding:0}#at-drawer.at4-recommended .at4-recommended-item .sponsored-label{margin:2px 0 0 21px;color:#ddd}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item{position:relative;padding:0;width:20pc;height:180px;margin:0}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img a:after{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.65);z-index:1000000;transition:all .2s ease-in-out}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item.at-hover .at4-recommended-item-img a:after{background:rgba(0,0,0,.8)}#at-drawer .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img,#at-drawer .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img a,#at-drawer .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img img{width:20pc;height:180px;float:none}#at-drawer .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption{width:100%;position:absolute;bottom:0;left:0;height:70px}#at-drawer .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption .at-h4{color:#fff;position:absolute;height:52px;top:0;left:20px;right:20px;margin:0;padding:0;line-height:25px;font-size:20px;font-weight:600;z-index:1000001;text-decoration:none;text-transform:none}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption .at-h4 a:hover{text-decoration:none}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption .at-h4 a:link{color:#fff}#at-drawer.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption small{position:absolute;top:auto;bottom:10px;left:20px;width:auto;color:#ccc}#at-drawer.at4-recommended .at4-logo-container{margin-left:20px}#at-drawer.ats-dark.at4-recommended .at4-logo-container a:hover{color:#fff}#at-drawer.at4-recommended .at-logo{margin:0}</style><style type="text/css">.at4-follow.at-mobile{display:none!important}.at4-follow{position:fixed;top:0;right:0;font-weight:400;color:#666;cursor:default;z-index:10001}.at4-follow .at4-follow-inner{position:relative;padding:10px 24px 10px 15px}.at4-follow-inner,.at-follow-open-control{border:0 solid #c5c5c5;border-width:1px 0 1px 1px;margin-top:-1px}.at4-follow .at4-follow-container{margin-left:9pt}.at4-follow.at4-follow-24 .at4-follow-container{height:24px;line-height:23px;font-size:13px}.at4-follow.at4-follow-32 .at4-follow-container{width:15pc;height:2pc;line-height:2pc;font-size:14px}.at4-follow .at4-follow-container .at-follow-label{display:inline-block;height:24px;line-height:24px;margin-right:10px;padding:0;cursor:default;float:left}.at4-follow .at4-follow-container .at-icon-wrapper{height:24px;width:24px}.at4-follow.ats-transparent .at4-follow-inner,.at-follow-open-control.ats-transparent{border-color:transparent}.at4-follow.ats-dark .at4-follow-inner,.at-follow-open-control.ats-dark{background:#262b30;border-color:#000;color:#fff}.at4-follow.ats-dark .at-follow-close-control{background-color:#262b30}.at4-follow.ats-light .at4-follow-inner{background:#fff;border-color:#c5c5c5}.at4-follow.ats-gray .at4-follow-inner,.at-follow-open-control.ats-gray{background:#f2f2f2;border-color:#c5c5c5}.at4-follow.ats-light .at4-follow-close-control,.at-follow-open-control.ats-light{background:#e5e5e5}.at4-follow .at4-follow-inner .at4-follow-close-control{position:absolute;top:0;bottom:0;left:0;width:20px;cursor:pointer;display:none}.at4-follow .at4-follow-inner .at4-follow-close-control div{display:block;line-height:20px;text-indent:-9999em;margin-top:calc(50% + 1px);overflow:hidden}.at-follow-open-control div.at4-arrow.at-left{background-position:0 -2px}.at-follow-open-control{position:fixed;height:35px;top:0;right:0;padding-top:10px;z-index:10002}.at-follow-btn{margin:0 5px 5px 0;padding:0;outline-offset:-1px;display:inline-block;box-sizing:content-box;transition:all .2s ease-in-out}.at-follow-btn:focus,.at-follow-btn:hover{transform:translateY(-4px)}.at4-follow-24 .at-follow-btn{height:25px;line-height:0;width:25px}</style><style type="text/css">.at-follow-tbx-element .at300b,.at-follow-tbx-element .at300m{display:inline-block;width:auto;padding:0;margin:0 2px 5px;outline-offset:-1px;transition:all .2s ease-in-out}.at-follow-tbx-element .at300b:focus,.at-follow-tbx-element .at300b:hover,.at-follow-tbx-element .at300m:focus,.at-follow-tbx-element .at300m:hover{transform:translateY(-4px)}.at-follow-tbx-element .addthis_vertical_style .at300b,.at-follow-tbx-element .addthis_vertical_style .at300m{display:block}.at-follow-tbx-element .addthis_vertical_style .at300b .addthis_follow_label,.at-follow-tbx-element .addthis_vertical_style .at300b .at-icon-wrapper,.at-follow-tbx-element .addthis_vertical_style .at300m .addthis_follow_label,.at-follow-tbx-element .addthis_vertical_style .at300m .at-icon-wrapper{display:inline-block;vertical-align:middle;margin-right:5px}.at-follow-tbx-element .addthis_vertical_style .at300b:focus,.at-follow-tbx-element .addthis_vertical_style .at300b:hover,.at-follow-tbx-element .addthis_vertical_style .at300m:focus,.at-follow-tbx-element .addthis_vertical_style .at300m:hover{transform:none}</style><style type="text/css">.at4-jumboshare .at-share-btn{display:inline-block;margin-right:13px;margin-top:13px}.at4-jumboshare .at-share-btn .at-icon{float:left}.at4-jumboshare .at-share-btn .at300bs{display:inline-block;float:left;cursor:pointer}.at4-jumboshare .at4-mobile .at-share-btn .at-icon,.at4-jumboshare .at4-mobile .at-share-btn .at-icon-wrapper{margin:0;padding:0}.at4-jumboshare .at4-mobile .at-share-btn{padding:0}.at4-jumboshare .at4-mobile .at-share-btn .at-label{display:none}.at4-jumboshare .at4-count{font-size:60px;line-height:60px;font-family:Helvetica neue,arial;font-weight:700}.at4-jumboshare .at4-count-container{display:table-cell;text-align:center;min-width:200px;vertical-align:middle;border-right:1px solid #ccc;padding-right:20px}.at4-jumboshare .at4-share-container{display:table-cell;vertical-align:middle;padding-left:20px}.at4-jumboshare .at4-share-container.at-share-tbx-element{padding-top:0}.at4-jumboshare .at4-title{position:relative;font-size:18px;line-height:18px;bottom:2px}.at4-jumboshare .at4-spacer{height:1px;display:block;visibility:hidden;opacity:0}.at4-jumboshare .at-share-btn{display:inline-block;margin:0 2px;line-height:0;padding:0;overflow:hidden;text-decoration:none;text-transform:none;color:#fff;cursor:pointer;transition:all .2s ease-in-out;border:0;background-color:transparent}.at4-jumboshare .at-share-btn:focus,.at4-jumboshare .at-share-btn:hover{transform:translateY(-4px);color:#fff;text-decoration:none}.at4-jumboshare .at-label{font-family:helvetica neue,helvetica,arial,sans-serif;font-size:9pt;padding:0 15px 0 0;margin:0;height:2pc;line-height:2pc;background:none}.at4-jumboshare .at-share-btn:hover,.at4-jumboshare .at-share-btn:link{text-decoration:none}.at4-jumboshare .at-share-btn::-moz-focus-inner{border:0;padding:0}.at4-jumboshare.at-mobile .at-label{display:none}</style><style type="text/css">.at4-recommendedbox-outer-container{display:inline}.at4-recommended-outer{position:static}.at4-recommended{top:20%;margin:0;text-align:center;font-weight:400;font-size:13px;line-height:17px;color:#666}.at4-recommended.at-inline .at4-recommended-horizontal{text-align:left}.at4-recommended-recommendedbox{padding:0;z-index:inherit}.at4-recommended-recommended{padding:40px 0}.at4-recommended-horizontal{max-height:340px}.at4-recommended.at-medium .at4-recommended-horizontal{max-height:15pc}.at4-recommended.at4-minimal.at-medium .at4-recommended-horizontal{padding-top:10px;max-height:230px}.at4-recommended-text-only .at4-recommended-horizontal{max-height:130px}.at4-recommended-horizontal{padding-top:5px;overflow-y:hidden}.at4-minimal{background:none;color:#000;border:none!important;box-shadow:none!important}@media screen and (max-width:900px){.at4-recommended-horizontal .at4-recommended-item,.at4-recommended-horizontal .at4-recommended-item .at4-recommended-item-img{width:15pc}}.at4-recommended.at4-minimal .at4-recommended-horizontal .at4-recommended-item .at4-recommended-item-caption{padding:0 0 10px}.at4-recommended.at4-minimal .at4-recommended-horizontal .at4-recommended-item-caption{padding:20px 0 0!important}.addthis-smartlayers .at4-recommended .at-h3.at-recommended-label{margin:0;padding:0;font-weight:300;font-size:18px;line-height:24px;color:#464646;width:100%;display:inline-block;zoom:1}.addthis-smartlayers .at4-recommended.at-inline .at-h3.at-recommended-label{text-align:left}#at4-thankyou .addthis-smartlayers .at4-recommended.at-inline .at-h3.at-recommended-label{text-align:center}.at4-recommended .at4-recommended-item{display:inline-block;zoom:1;position:relative;background:#fff;border:1px solid #c5c5c5;width:200px;margin:10px}.addthis_recommended_horizontal .at4-recommended-item{border:none}.at4-recommended .at4-recommended-item .sponsored-label{color:#666;font-size:9px;position:absolute;top:-20px}.at4-recommended .at4-recommended-item-img .at-tli,.at4-recommended .at4-recommended-item-img a{position:absolute;left:0}.at4-recommended.at-inline .at4-recommended-horizontal .at4-recommended-item{margin:10px 20px 0 0}.at4-recommended.at-medium .at4-recommended-horizontal .at4-recommended-item{margin:10px 10px 0 0}.at4-recommended.at-medium .at4-recommended-item{width:140px;overflow:hidden}.at4-recommended .at4-recommended-item .at4-recommended-item-img{position:relative;text-align:center;width:100%;height:200px;line-height:0;overflow:hidden}.at4-recommended .at4-recommended-item .at4-recommended-item-img a{display:block;width:100%;height:200px}.at4-recommended.at-medium .at4-recommended-item .at4-recommended-item-img,.at4-recommended.at-medium .at4-recommended-item .at4-recommended-item-img a{height:140px}.at4-recommended .at4-recommended-item .at4-recommended-item-img img{position:absolute;top:0;left:0;min-height:0;min-width:0;max-height:none;max-width:none;margin:0;padding:0}.at4-recommended .at4-recommended-item .at4-recommended-item-caption{height:74px;overflow:hidden;padding:20px;text-align:left;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}.at4-recommended.at-medium .at4-recommended-item .at4-recommended-item-caption{height:50px;padding:15px}.at4-recommended .at4-recommended-item .at4-recommended-item-caption .at-h4{height:54px;margin:0 0 5px;padding:0;overflow:hidden;word-wrap:break-word;font-size:14px;font-weight:400;line-height:18px;text-align:left}.at4-recommended.at-medium .at4-recommended-item .at4-recommended-item-caption .at-h4{font-size:9pt;line-height:1pc;height:33px}.at4-recommended .at4-recommended-item:hover .at4-recommended-item-caption .at-h4{text-decoration:underline}.at4-recommended a:link,.at4-recommended a:visited{text-decoration:none;color:#464646}.at4-recommended .at4-recommended-item .at4-recommended-item-caption .at-h4 a:hover{text-decoration:underline;color:#000}.at4-recommended .at4-recommended-item .at4-recommended-item-caption small{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:11px;color:#666}.at4-recommended.at-medium .at4-recommended-item .at4-recommended-item-caption small{font-size:9px}.at4-recommended .at4-recommended-vertical{padding:15px 0 0}.at4-recommended .at4-recommended-vertical .at4-recommended-item{display:block;width:auto;max-width:100%;height:60px;border:none;margin:0 0 15px;box-shadow:none;background:none}.at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img,.at4-recommended-vertical .at4-recommended-item .at4-recommended-item-img img{width:60px;height:60px;float:left}.at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption{border-top:none;margin:0;height:60px;padding:3px 5px}.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption .at-h4{height:38px;margin:0}.at4-recommended .at4-recommended-vertical .at4-recommended-item .at4-recommended-item-caption small{position:absolute;bottom:0}.at4-recommended .at-recommended-label.at-vertical{text-align:left}.at4-no-image-light-recommended,.at4-no-image-minimal-recommended{background-color:#f2f2f2!important}.at4-no-image-gray-recommended{background-color:#e6e6e5!important}.at4-no-image-dark-recommended{background-color:#4e555e!important}.at4-recommended .at4-recommended-item-placeholder-img{background-repeat:no-repeat!important;background-position:center!important;width:100%!important;height:100%!important}.at4-recommended-horizontal .at4-no-image-dark-recommended .at4-recommended-item-placeholder-img{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAfCAYAAACCox+xAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjlFNUUyQTg3MTI0RDExRTM4NzAwREJDRjlCQzAyMUVFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjlFNUUyQTg4MTI0RDExRTM4NzAwREJDRjlCQzAyMUVFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6OUU1RTJBODUxMjREMTFFMzg3MDBEQkNGOUJDMDIxRUUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6OUU1RTJBODYxMjREMTFFMzg3MDBEQkNGOUJDMDIxRUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6oCfPiAAABfUlEQVR42uyWTU/DMAyGm3bdBxp062hHe+PC//9HCIkDYpNAO7CPAuWN5Eohyhpno2GHWqq8pO78xHHsiLquH4L/l6cwuBAZaOPKs//YBFIJIR59UiAt7huYi90aE/UQakTDLaL26RUEAAJqiefm93T9Bpj1X4O0bY0OIUXCpYBJvYDAUWyAUCWliHGTcnpqRMaM72ImRAJVknYG+eb4YEDIBeU0zGnsBLK1ODogYSsLhDwIJeVVk18lzfNA4ERGZNXi59UCIQhiYDilpSm/jp4awLxDvWhlf4/nGe8+LLuSt+SZul28ggaHG6gNVhDR+IuRFzOoxGKWwG7vVFm5AAQxgcqYpzrjFjR9zwPH5LSuT7XlNr2MQm5LzqjLpncNNaM+s8M27Y60g3FwhoSMzrtUQllgLtRs5pZ2cB4IhbvQbGRZv1NsrhyS8+SI5Mo9RJWpjAI1xqKL+0iEP180vy214JbeR12AyOgsHI7e0NfFyKv0ID1ID+IqPwIMAOeljGQOryBmAAAAAElFTkSuQmCC)!important}.at4-recommended-vertical .at4-no-image-dark-recommended .at4-recommended-item-placeholder-img{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAOCAYAAADwikbvAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjAzREMyNTM2MTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjAzREMyNTM3MTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MDNEQzI1MzQxMjRGMTFFMzg3MDBEQkNGOUJDMDIxRUUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MDNEQzI1MzUxMjRGMTFFMzg3MDBEQkNGOUJDMDIxRUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5GfbtkAAAAxklEQVR42qRSTQvCMAxduk53mEOHKFPP/v8/5cGTiIibivVFUomlG7gFHvloXpKmJefcPhkmNyvGEWj+IOZA6ckPImoxxVwOLvCvXUzkpayNCpRQK64IbOBnAYGAXMeMslNlU+CzrIEdCkxi5DPAoz6BE8ZuVNdKJuL8rS9sv62IXlCHyP0KqKUKZXK9uwkSLVArfwpVR3b225kXwovibcP+jC4jUtfWPZmfqJJnYlkAM128j1z0nHWKSUbIKDL/msHktwADAPptQo+vkZNLAAAAAElFTkSuQmCC)!important}.at4-recommended-horizontal .at4-no-image-gray-recommended .at4-recommended-item-placeholder-img,.at4-recommended-horizontal .at4-no-image-light-recommended .at4-recommended-item-placeholder-img,.at4-recommended-horizontal .at4-no-image-minimal-recommended .at4-recommended-item-placeholder-img{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAfCAYAAACCox+xAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjAzREMyNTMyMTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjAzREMyNTMzMTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6OUU1RTJBODkxMjREMTFFMzg3MDBEQkNGOUJDMDIxRUUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6OUU1RTJBOEExMjREMTFFMzg3MDBEQkNGOUJDMDIxRUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6dfDQvAAABg0lEQVR42uyWS0vDQBDH82jaKNW0qUltbl68e/Di98eLBz+CCB5EBaWIpUat/4UJLMuame1j7SEDYbqbKfPLvHbDi8ur8+D/5T4K9kR6xrr27D+xgdS3N9d3PilQFmcNzN6mxkbdhxrQcoGofXkFAUAINcVzrG2vsP8KmJdtg7SlxoRQouBywOReQOAosUDoklPEpEU5XDciqeB/iRAig6pIO4P8CHysBBDqg0palrR2Alkwjj5RsDUDoRqhorpq6quifRkInKiIPLf4eWIgQoLoWbq0stXXn10DmDeoR2PsL/E84N0Hk5Wypc70dMkGGhzOoeb4gpjW34K6GEFljFkGu6XTZJUCEMQBVCHs6kI60MycB47FyUmo20oPvYJCzhVnvIsR3zg5ghoRTNpyHKTBBhIJTt6pFsoZ9iLDZswcB5uBULhnho0a66eazaFDca59Hym1e4guQ4rCO4Fu/T4Sw8Gk+c3MghN6H+8CRKVg4tB6fV8XI6/SgXQgHYir/AowAMU5TskhKVUNAAAAAElFTkSuQmCC)!important}.at4-recommended-vertical .at4-no-image-gray-recommended .at4-recommended-item-placeholder-img,.at4-recommended-vertical .at4-no-image-light-recommended .at4-recommended-item-placeholder-img,.at4-recommended-vertical .at4-no-image-minimal-recommended .at4-recommended-item-placeholder-img{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAOCAYAAADwikbvAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjAzREMyNTNBMTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjAzREMyNTNCMTI0RjExRTM4NzAwREJDRjlCQzAyMUVFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MDNEQzI1MzgxMjRGMTFFMzg3MDBEQkNGOUJDMDIxRUUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MDNEQzI1MzkxMjRGMTFFMzg3MDBEQkNGOUJDMDIxRUUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz65Fr9cAAAA0ElEQVR42qRRuQrCQBDd3SSaIgYNosSrtLew8f+xsfAnYmEVRMR4YHwjExjCbsBk4DHHzptjR2+2u7VqJ3efjTNQ/EEMgbgiv46H/QNTDPnhCv/mYiLPI21EIIaaUEVgBj+oETQQypgRtidsXfNJpsACBXo28gWgUd9AjrEL0TXhiSh/XhWudlZI/kCdLPtFUGMRCni9p6kl+kAq/D5UavmzX2fNd87obsCSfztnrOR0rjvTiRImkoyAQQNRyZ2jhjenGNVBOpF1WZatyV8BBgBJ+irgS/KHdAAAAABJRU5ErkJggg==)!important}#at-drawer.ats-dark,.at4-recommended.ats-dark .at4-recommended-horizontal .at4-recommended-item-caption,.at4-recommended.ats-dark .at4-recommended-vertical .at4-recommended-item-caption{background:#262b30}#at-drawer.ats-gray,.at4-recommended.ats-gray .at4-recommended-horizontal .at4-recommended-item-caption{background:#f2f2f2}#at-drawer.ats-light,.at4-recommended.ats-light .at4-recommended-horizontal .at4-recommended-item-caption{background:#fff}.at4-recommended.ats-dark .at4-recommended-vertical .at4-recommended-item{background:none}.at4-recommended.ats-dark .at4-recommended-item .at4-recommended-item-caption a:hover,.at4-recommended.ats-dark .at4-recommended-item .at4-recommended-item-caption a:link,.at4-recommended.ats-dark .at4-recommended-item .at4-recommended-item-caption a:visited,.at4-recommended.ats-dark .at4-recommended-item .at4-recommended-item-caption small,.at4-recommended.ats-dark .at4-recommended-item-caption,.at4-recommended.ats-dark .at-logo a:hover,.at4-recommended.ats-dark .at-recommended-label.at-vertical{color:#fff}.at4-recommended-vertical-logo{padding-top:0;text-align:left}.at4-recommended-vertical-logo .at4-logo-container{line-height:10px}.at4-recommended-horizontal-logo{text-align:center}.at4-recommended.at-inline .at4-recommended-horizontal-logo{text-align:left}#at4-thankyou .at4-recommended.at-inline .at4-recommended-horizontal{text-align:center}.at4-recommended .at-logo{margin:10px 0 0;padding:0;height:25px;overflow:auto;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}.at4-recommended.at-inline .at4-recommended-horizontal .at-logo{text-align:left}.at4-recommended .at4-logo-container a.at-sponsored-link{color:#666}.at4-recommended-class .at4-logo-container a:hover,.at4-recommendedbox-outer-container .at4-recommended-recommendedbox .at4-logo-container a:hover{color:#000}</style><style type="text/css">.at-recommendedjumbo-outer-container{margin:0;padding:0;border:0;background:none;color:#000}.at-recommendedjumbo-footer{position:relative;width:100%;height:510px;overflow:hidden;transition:all .3s ease-in-out}.at-mobile .at-recommendedjumbo-footer{height:250px}.at-recommendedjumbo-footer #bg-link:after{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.75)}.at-recommendedjumbo-footer:hover #bg-link:after{background:rgba(0,0,0,.85)}.at-recommendedjumbo-footer *,.at-recommendedjumbo-footer :after,.at-recommendedjumbo-footer :before{box-sizing:border-box}.at-recommendedjumbo-footer:hover #at-recommendedjumbo-footer-bg{animation:atRecommendedJumboAnimatedBackground 1s ease-in-out 1;animation-fill-mode:forwards}.at-recommendedjumbo-footer #at-recommendedjumbo-top-holder{position:absolute;top:0;padding:0 40px;width:100%}.at-mobile .at-recommendedjumbo-footer #at-recommendedjumbo-top-holder{padding:0 20px}.at-recommendedjumbo-footer .at-recommendedjumbo-footer-inner{position:relative;text-align:center;font-family:helvetica,arial,sans-serif;z-index:2;width:100%}.at-recommendedjumbo-footer #at-recommendedjumbo-label-holder{margin:40px 0 0;max-height:30px}.at-mobile .at-recommendedjumbo-footer #at-recommendedjumbo-label-holder{margin:20px 0 0;max-height:20px}.at-recommendedjumbo-footer #at-recommendedjumbo-label{font-weight:300;font-size:24px;line-height:24px;color:#fff;margin:0}.at-mobile .at-recommendedjumbo-footer #at-recommendedjumbo-label{font-weight:150;font-size:14px;line-height:14px}.at-recommendedjumbo-footer #at-recommendedjumbo-title-holder{margin:20px 0 0;min-height:3pc;max-height:78pt}.at-mobile .at-recommendedjumbo-footer #at-recommendedjumbo-title-holder{margin:10px 0 0;min-height:24px;max-height:54px}.at-recommendedjumbo-footer #at-recommendedjumbo-content-title{font-size:3pc;line-height:52px;font-weight:700;margin:0}.at-mobile .at-recommendedjumbo-footer #at-recommendedjumbo-content-title{font-size:24px;line-height:27px}.at-recommendedjumbo-footer a{text-decoration:none;color:#fff}.at-recommendedjumbo-footer a:visited{color:#fff}.at-recommendedjumbo-footer small{margin:20px 0 0;display:inline-block;height:2pc;line-height:2pc;font-size:14px;color:#ccc;cursor:default}.at-mobile .at-recommendedjumbo-footer small{margin:10px 0 0;height:14px;line-height:14px;font-size:9pt}.at-recommendedjumbo-footer .at-logo-container{position:absolute;bottom:20px;margin:auto;left:0;right:0}.at-mobile .at-recommendedjumbo-footer .at-logo-container{bottom:10px}.at-recommendedjumbo-footer a.at-sponsored-link{color:#ccc}.at-recommendedjumbo-footer div #at-recommendedjumbo-logo-link{padding:2px 0 0 11px;text-decoration:none;line-height:20px;font-family:helvetica,arial,sans-serif;font-size:9px;color:#ccc}@keyframes atRecommendedJumboAnimatedBackground{0%{transform:scale(1,1)}to{transform:scale(1.1,1.1)}}</style><style type="text/css">.at-resp-share-element{position:relative;padding:0;margin:0;font-size:0;line-height:0}.at-resp-share-element:after,.at-resp-share-element:before{content:" ";display:table}.at-resp-share-element.at-mobile .at4-share-count-container,.at-resp-share-element.at-mobile .at-label{display:none}.at-resp-share-element .at-share-btn{display:inline-block;*display:inline;*zoom:1;margin:0 2px 5px;padding:0;overflow:hidden;line-height:0;text-decoration:none;text-transform:none;color:#fff;cursor:pointer;transition:all .2s ease-in-out;border:0;font-family:helvetica neue,helvetica,arial,sans-serif;background-color:transparent}.at-resp-share-element .at-share-btn::-moz-focus-inner{border:0;padding:0}.at-resp-share-element .at-share-btn:focus,.at-resp-share-element .at-share-btn:hover{transform:translateY(-4px);color:#fff;text-decoration:none}.at-resp-share-element .at-share-btn .at-icon-wrapper{float:left}.at-resp-share-element .at-share-btn.at-share-btn.at-svc-compact:hover{transform:none}.at-resp-share-element .at-share-btn .at-label{font-family:helvetica neue,helvetica,arial,sans-serif;font-size:9pt;padding:0 15px 0 0;margin:0 0 0 5px;height:2pc;line-height:2pc;background:none}.at-resp-share-element .at-icon,.at-resp-share-element .at-label{cursor:pointer}.at-resp-share-element .at4-share-count-container{text-decoration:none;float:right;padding-right:15px;font-size:9pt}.at-mobile .at-resp-share-element .at-label{display:none}.at-resp-share-element.at-mobile .at-share-btn{margin-right:5px}.at-mobile .at-resp-share-element .at-share-btn{padding:5px;margin-right:5px}</style><style type="text/css">.at-share-tbx-element{position:relative;margin:0;color:#fff;font-size:0}.at-share-tbx-element,.at-share-tbx-element .at-share-btn{font-family:helvetica neue,helvetica,arial,sans-serif;padding:0;line-height:0}.at-share-tbx-element .at-share-btn{cursor:pointer;margin:0 5px 5px 0;display:inline-block;overflow:hidden;border:0;text-decoration:none;text-transform:none;background-color:transparent;color:inherit;transition:all .2s ease-in-out}.at-share-tbx-element .at-share-btn:focus,.at-share-tbx-element .at-share-btn:hover{transform:translateY(-4px);outline-offset:-1px;color:inherit}.at-share-tbx-element .at-share-btn::-moz-focus-inner{border:0;padding:0}.at-share-tbx-element .at-share-btn.at-share-btn.at-svc-compact:hover{transform:none}.at-share-tbx-element .at-icon-wrapper{vertical-align:middle}.at-share-tbx-element .at4-share-count,.at-share-tbx-element .at-label{margin:0 7.5px 0 2.5px;text-decoration:none;vertical-align:middle;display:inline-block;background:none;height:0;font-size:inherit;line-height:inherit;color:inherit}.at-share-tbx-element.at-mobile .at4-share-count,.at-share-tbx-element.at-mobile .at-label{display:none}.at-share-tbx-element .at_native_button{vertical-align:middle}.at-share-tbx-element .addthis_counter.addthis_bubble_style{margin:0 2px;vertical-align:middle;display:inline-block}.at-share-tbx-element .fb_iframe_widget{display:block}.at-share-tbx-element.at-share-tbx-native .at300b{vertical-align:middle}.at-style-responsive .at-share-btn{padding:5px}.at-style-jumbo{display:table}.at-style-jumbo .at4-spacer{height:1px;display:block;visibility:hidden;opacity:0}.at-style-jumbo .at4-count-container{display:table-cell;text-align:center;min-width:200px;vertical-align:middle;border-right:1px solid #ccc;padding-right:20px}.at-style-jumbo .at4-count{font-size:60px;line-height:60px;font-weight:700}.at-style-jumbo .at4-count-title{position:relative;font-size:18px;line-height:18px;bottom:2px}.at-style-jumbo .at-share-btn-elements{display:table-cell;vertical-align:middle;padding-left:20px}.at_flat_counter{cursor:pointer;font-family:helvetica,arial,sans-serif;font-weight:700;text-transform:uppercase;display:inline-block;position:relative;vertical-align:top;height:auto;margin:0 5px;padding:0 6px;left:-1px;background:#ebebeb;color:#32363b;transition:all .2s ease}.at_flat_counter:after{top:30%;left:-4px;content:"";position:absolute;border-width:5px 8px 5px 0;border-style:solid;border-color:transparent #ebebeb transparent transparent;display:block;width:0;height:0;transform:translateY(360deg)}.at_flat_counter:hover{background:#e1e2e2}</style><style type="text/css">.at4-thankyou-background{top:0;right:0;left:0;bottom:0;-webkit-overflow-scrolling:touch;z-index:9999999;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpizCuu/sRABGBiIBKMKqSOQoAAAwC8KgJipENhxwAAAABJRU5ErkJggg==);background:hsla(217,6%,46%,.95)}.at4-thankyou-background.at-thankyou-shown{position:fixed}.at4-thankyou-inner{position:absolute;width:100%;top:10%;left:50%;margin-left:-50%;text-align:center}.at4-thankyou-mobile .at4-thankyou-inner{top:5%}.thankyou-description{font-weight:400}.at4-thankyou-background .at4lb-inner{position:relative;width:100%;height:100%}.at4-thankyou-background .at4lb-inner .at4x{position:absolute;top:15px;right:15px;display:block;width:20px;height:20px;padding:20px;margin:0;cursor:pointer;transition:opacity .25s ease-in;opacity:.4;background:url("data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAAWdEVYdENyZWF0aW9uIFRpbWUAMTEvMTMvMTKswDp5AAAAd0lEQVQ4jb2VQRLAIAgDE///Z3qqY1FAhalHMCsCIkVEAIAkkVgvp2lDBgYAnAyHkWotLccNrEd4A7X2TqIdqLfnWBAdaF5rJdyJfjtPH5GT37CaGhoVq3nOm/XflUuLUto2pY1d+vRKh0Pp+MrAVtDe2JkvYNQ+jVSEEFmOkggAAAAASUVORK5CYII=") no-repeat center center;overflow:hidden;text-indent:-99999em;border:1px solid transparent}.at4-thankyou-background .at4lb-inner .at4x:focus,.at4-thankyou-background .at4lb-inner .at4x:hover{border:1px solid #fff;border-radius:50%;outline:0}.at4-thankyou-background .at4lb-inner #at4-palogo{position:absolute;bottom:10px;display:inline-block;text-decoration:none;font-family:helvetica,arial,sans-serif;font-size:11px;cursor:pointer;-webkit-transition:opacity .25s ease-in;moz-transition:opacity .25s ease-in;transition:opacity .25s ease-in;opacity:.5;z-index:100020;color:#fff;padding:2px 0 0 13px}.at4-thankyou-background .at4lb-inner #at4-palogo .at-branding-addthis,.at4-thankyou-background .at4lb-inner #at4-palogo .at-branding-info{color:#fff}.at4-thankyou-background .at4lb-inner #at4-palogo:hover,.at4-thankyou-background.ats-dark .at4lb-inner a#at4-palogo:hover{text-decoration:none;color:#fff;opacity:1}.at4-thankyou-background.ats-dark{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgeMZABGBiIBKMKqSOQoAAAwB+cQD6hqlbCwAAAABJRU5ErkJggg==");background:rgba(0,0,0,.85)}.at4-thankyou-background .thankyou-title{color:#fff;font-size:38.5px;margin:10px 20px;line-height:38.5px;font-family:helvetica neue,helvetica,arial,sans-serif;font-weight:300}.at4-thankyou-background.ats-dark .thankyou-description,.at4-thankyou-background.ats-dark .thankyou-title{color:#fff}.at4-thankyou-background .thankyou-description{color:#fff;font-size:18px;margin:10px 0;line-height:24px;padding:0;font-family:helvetica neue,helvetica,arial,sans-serif;font-weight:300}.at4-thankyou-background .at4-thanks-icons{padding-top:10px}.at4-thankyou-mobile *{-webkit-overflow-scrolling:touch}#at4-thankyou .at4-recommended-recommendedbox .at-logo{display:none}.at4-thankyou .at-h3{height:49px;line-height:49px;margin:0 50px 0 20px;padding:1px 0 0;font-family:helvetica neue,helvetica,arial,sans-serif;font-size:1pc;font-weight:700;color:#fff;text-shadow:0 1px #000}.at4-thanks{padding-top:50px;text-align:center}.at4-thanks label{display:block;margin:0 0 15px;font-size:1pc;line-height:1pc}.at4-thanks .at4-h2{background:none;border:none;margin:0 0 10px;padding:0;font-family:helvetica neue,helvetica,arial,sans-serif;font-size:28px;font-weight:300;color:#000}.at4-thanks .at4-thanks-icons{position:relative;height:2pc}.at4-thanks .at4-thanks-icons .at-thankyou-label{display:block;padding-bottom:10px;font-size:14px;color:#666}.at4-thankyou-layer .at-follow .at-icon-wrapper{width:2pc;height:2pc}</style><style type="text/css">.at4-recommended-toaster{position:fixed;top:auto;bottom:0;right:0;z-index:100021}.at4-recommended-toaster.ats-light{border:1px solid #c5c5c5;background:#fff}.at4-recommended-toaster.ats-gray{border:1px solid #c5c5c5;background:#f2f2f2}.at4-recommended-toaster.ats-dark{background:#262b30;color:#fff}.at4-recommended-toaster .at4-recommended-container{padding-top:0;margin:0}.at4-recommended.at4-recommended-toaster div.at-recommended-label{line-height:1pc;font-size:1pc;text-align:left;padding:20px 0 0 20px}.at4-toaster-outer .at4-recommended .at4-recommended-item .at4-recommended-item-caption .at-h4{font-size:11px;line-height:11px;margin:10px 0 6px;height:30px}.at4-recommended.at4-recommended-toaster div.at-recommended-label.ats-gray,.at4-recommended.at4-recommended-toaster div.at-recommended-label.ats-light{color:#464646}.at4-recommended.at4-recommended-toaster div.at-recommended-label.ats-dark{color:#fff}.at4-toaster-close-control{position:absolute;top:0;right:0;display:block;width:20px;height:20px;line-height:20px;margin:5px 5px 0 0;padding:0;text-indent:-9999em}.at4-toaster-open-control{position:fixed;right:0;bottom:0;z-index:100020}.at4-toaster-outer .at4-recommended-item{width:90pt;border:0;margin:9px 10px 0}.at4-toaster-outer .at4-recommended-item:first-child{margin-left:20px}.at4-toaster-outer .at4-recommended-item:last-child{margin-right:20px}.at4-toaster-outer .at4-recommended-item .at4-recommended-item-img{max-height:90pt;max-width:90pt}.at4-toaster-outer .at4-recommended-item .at4-recommended-item-img img{height:90pt;width:90pt}.at4-toaster-outer .at4-recommended-item .at4-recommended-item-caption{height:30px;padding:0;margin:0;height:initial}.at4-toaster-outer .ats-dark .at4-recommended-item .at4-recommended-item-caption{background:#262b30}.at4-toaster-outer .at4-recommended .at4-recommended-item .at4-recommended-item-caption small{width:auto;line-height:14px;margin:0}.at4-toaster-outer .at4-recommended.ats-dark .at4-recommended-item .at4-recommended-item-caption small{color:#fff}.at4-recommended-toaster .at-logo{margin:0 0 3px 20px;text-align:left}.at4-recommended-toaster .at-logo .at4-logo-container.at-sponsored-logo{position:relative}.at4-toaster-outer .at4-recommended-item .sponsored-label{text-align:right;font-size:10px;color:#666;float:right;position:fixed;bottom:6px;right:20px;top:initial;z-index:99999}</style><style type="text/css">.at4-whatsnext{position:fixed;bottom:0!important;right:0;background:#fff;border:1px solid #c5c5c5;margin:-1px;width:390px;height:90pt;overflow:hidden;font-size:9pt;font-weight:400;color:#000;z-index:1800000000}.at4-whatsnext a{color:#666}.at4-whatsnext .at-whatsnext-content{height:90pt;position:relative}.at4-whatsnext .at-whatsnext-content .at-branding{position:absolute;bottom:15px;right:10px;padding-left:9px;text-decoration:none;line-height:10px;font-family:helvetica,arial,sans-serif;font-size:10px;color:#666}.at4-whatsnext .at-whatsnext-content .at-whatsnext-content-inner{position:absolute;top:15px;right:20px;bottom:15px;left:140px;text-align:left;height:105px}.at4-whatsnext .at-whatsnext-content-inner a{display:inline-block}.at4-whatsnext .at-whatsnext-content-inner div.at-h6{text-align:left;margin:0;padding:0 0 3px;font-size:11px;color:#666;cursor:default}.at4-whatsnext .at-whatsnext-content .at-h3{text-align:left;margin:5px 0;padding:0;line-height:1.2em;font-weight:400;font-size:14px;height:3pc}.at4-whatsnext .at-whatsnext-content-inner a:link,.at4-whatsnext .at-whatsnext-content-inner a:visited{text-decoration:none;font-weight:400;color:#464646}.at4-whatsnext .at-whatsnext-content-inner a:hover{color:#000}.at4-whatsnext .at-whatsnext-content-inner small{position:absolute;bottom:15px;line-height:10px;font-size:11px;color:#666;cursor:default;text-align:left}.at4-whatsnext .at-whatsnext-content .at-whatsnext-content-img{position:absolute;top:0;left:0;width:90pt;height:90pt;overflow:hidden}.at4-whatsnext .at-whatsnext-content .at-whatsnext-content-img img{position:absolute;top:0;left:0;max-height:none;max-width:none}.at4-whatsnext .at-whatsnext-close-control{position:absolute;top:0;right:0;display:block;width:20px;height:20px;line-height:20px;margin:0 5px 0 0;padding:0;text-indent:-9999em}.at-whatsnext-open-control{position:fixed;right:0;bottom:0;z-index:100020}.at4-whatsnext.ats-dark{background:#262b30}.at4-whatsnext.ats-dark .at-whatsnext-content .at-h3,.at4-whatsnext.ats-dark .at-whatsnext-content a.at4-logo:hover,.at4-whatsnext.ats-dark .at-whatsnext-content-inner a:link,.at4-whatsnext.ats-dark .at-whatsnext-content-inner a:visited{color:#fff}.at4-whatsnext.ats-light{background:#fff}.at4-whatsnext.ats-gray{background:#f2f2f2}.at4-whatsnext.at-whatsnext-nophoto{width:270px}.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content-img{display:none}.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content .at-whatsnext-content-inner{top:15px;right:0;left:20px}.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content .at-whatsnext-content-inner.addthis_32x32_style{top:0;right:0;left:0;padding:45px 20px 0;font-size:20px}.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content .at-whatsnext-content-inner .at4-icon,.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content .at-whatsnext-content-inner .at4-icon-fw,.at4-whatsnext.at-whatsnext-nophoto .at-whatsnext-content .at-whatsnext-content-inner .whatsnext-msg{vertical-align:middle}.at-whatsnext-img,.at-whatsnext-img-lnk{position:absolute;left:0}</style><style type="text/css">.at4-whatsnextmobile{position:fixed;bottom:0;right:0;left:0;background:#fff;z-index:9999998;height:170px;font-size:28px}.at4-whatsnextmobile .col-2{height:100%;font-size:1em}.at4-whatsnextmobile .col-2:first-child{max-width:200px;display:inline-block;float:left}.at4-whatsnextmobile .col-2:last-child{position:absolute;left:200px;right:50px;top:0;bottom:0;display:inline-block}.at4-whatsnextmobile .at-whatsnext-content-inner{font-size:1em}.at4-whatsnextmobile .at-whatsnext-content-img img{height:100%;width:100%}.at4-whatsnextmobile .at-close-control{font-size:1em;position:absolute;top:0;right:0;width:50px;height:50px}.at4-whatsnextmobile .at-close-control button{width:100%;height:100%;font-size:1em;font-weight:400;text-decoration:none;opacity:.5;padding:0;cursor:pointer;background:0 0;border:0;-webkit-appearance:none}.at4-whatsnextmobile .at-h3,.at4-whatsnextmobile .at-h6{font-size:1em;margin:0;color:#a1a1a1;margin-left:2.5%;margin-top:25px}.at4-whatsnextmobile .at-h3{font-size:1em;line-height:1em;font-weight:500;height:50%}.at4-whatsnextmobile .at-h3 a{font-size:1em;text-decoration:none}.at4-whatsnextmobile .at-h6{font-size:.8em;line-height:.8em;font-weight:500}.at4-whatsnextmobile .footer{position:absolute;bottom:2px;left:200px;right:0;padding-left:2.5%;font-size:1em;line-height:.6em}.at4-whatsnextmobile .footer small{font-size:.6em;color:#a1a1a1}.at4-whatsnextmobile .footer small:first-child{margin-right:5%;float:left}.at4-whatsnextmobile .footer small:last-child{margin-right:2.5%;float:right}.at4-whatsnextmobile .at-whatsnext-content{height:100%}.at4-whatsnextmobile.ats-dark{background:#262b30;color:#fff}.at4-whatsnextmobile .at-close-control button{color:#bfbfbf}.at4-whatsnextmobile.ats-dark a:link,.at4-whatsnextmobile.ats-dark a:visited{color:#fff}.at4-whatsnextmobile.ats-gray{background:#f2f2f2;color:#262b30}.at4-whatsnextmobile.ats-light{background:#fff;color:#262b30}.at4-whatsnextmobile.ats-dark .footer a:link,.at4-whatsnextmobile.ats-dark .footer a:visited,.at4-whatsnextmobile.ats-gray .footer a:link,.at4-whatsnextmobile.ats-gray .footer a:visited,.at4-whatsnextmobile.ats-light .footer a:link,.at4-whatsnextmobile.ats-light .footer a:visited{color:#a1a1a1}.at4-whatsnextmobile.ats-gray a:link,.at4-whatsnextmobile.ats-gray a:visited,.at4-whatsnextmobile.ats-light a:link,.at4-whatsnextmobile.ats-light a:visited{color:#262b30}@media only screen and (min-device-width:320px) and (max-device-width:480px){.at4-whatsnextmobile{height:85px;font-size:14px}.at4-whatsnextmobile .col-2:first-child{width:75pt}.at4-whatsnextmobile .col-2:last-child{right:25px;left:75pt}.at4-whatsnextmobile .footer{left:75pt}.at4-whatsnextmobile .at-close-control{width:25px;height:25px}.at4-whatsnextmobile .at-h3,.at4-whatsnextmobile .at-h6{margin-top:12.5px}}</style><style type="text/css">.at-custom-mobile-bar{left:0;right:0;width:100%;height:56px;position:fixed;text-align:center;z-index:100020;background:#fff;overflow:hidden;box-shadow:0 0 10px 0 rgba(0,0,0,.2);font:initial;line-height:normal;top:auto;bottom:0}.at-custom-mobile-bar.at-custom-mobile-bar-zindex-hide{z-index:-1!important}.at-custom-mobile-bar.atss-top{top:0;bottom:auto}.at-custom-mobile-bar.atss-bottom{top:auto;bottom:0}.at-custom-mobile-bar .at-custom-mobile-bar-btns{display:inline-block;text-align:center}.at-custom-mobile-bar .at-custom-mobile-bar-counter,.at-custom-mobile-bar .at-share-btn{margin-top:4px}.at-custom-mobile-bar .at-share-btn{display:inline-block;text-decoration:none;transition:none;box-sizing:content-box}.at-custom-mobile-bar .at-custom-mobile-bar-counter{font-family:Helvetica neue,arial;vertical-align:top;margin-left:4px;margin-right:4px;display:inline-block}.at-custom-mobile-bar .at-custom-mobile-bar-count{font-size:26px;line-height:1.25em;color:#222}.at-custom-mobile-bar .at-custom-mobile-bar-text{font-size:9pt;line-height:1.25em;color:#888;letter-spacing:1px}.at-custom-mobile-bar .at-icon-wrapper{text-align:center;height:3pc;width:3pc;margin:0 4px}.at-custom-mobile-bar .at-icon{vertical-align:top;margin:8px;width:2pc;height:2pc}.at-custom-mobile-bar.at-shfs-medium{height:3pc}.at-custom-mobile-bar.at-shfs-medium .at-custom-mobile-bar-counter{margin-top:6px}.at-custom-mobile-bar.at-shfs-medium .at-custom-mobile-bar-count{font-size:18px}.at-custom-mobile-bar.at-shfs-medium .at-custom-mobile-bar-text{font-size:10px}.at-custom-mobile-bar.at-shfs-medium .at-icon-wrapper{height:40px;width:40px}.at-custom-mobile-bar.at-shfs-medium .at-icon{margin:6px;width:28px;height:28px}.at-custom-mobile-bar.at-shfs-small{height:40px}.at-custom-mobile-bar.at-shfs-small .at-custom-mobile-bar-counter{margin-top:3px}.at-custom-mobile-bar.at-shfs-small .at-custom-mobile-bar-count{font-size:1pc}.at-custom-mobile-bar.at-shfs-small .at-custom-mobile-bar-text{font-size:10px}.at-custom-mobile-bar.at-shfs-small .at-icon-wrapper{height:2pc;width:2pc}.at-custom-mobile-bar.at-shfs-small .at-icon{margin:4px;width:24px;height:24px}</style><style type="text/css">.at-custom-sidebar{top:20%;width:58px;position:fixed;text-align:center;z-index:100020;background:#fff;overflow:hidden;box-shadow:0 0 10px 0 rgba(0,0,0,.2);font:initial;line-height:normal;top:auto;bottom:0}.at-custom-sidebar.at-custom-sidebar-zindex-hide{z-index:-1!important}.at-custom-sidebar.atss-left{left:0;right:auto;float:left;border-radius:0 4px 4px 0}.at-custom-sidebar.atss-right{left:auto;right:0;float:right;border-radius:4px 0 0 4px}.at-custom-sidebar .at-custom-sidebar-btns{display:inline-block;text-align:center;padding-top:4px}.at-custom-sidebar .at-custom-sidebar-counter{margin-bottom:8px}.at-custom-sidebar .at-share-btn{display:inline-block;text-decoration:none;transition:none;box-sizing:content-box}.at-custom-sidebar .at-custom-sidebar-counter{font-family:Helvetica neue,arial;vertical-align:top;margin-left:4px;margin-right:4px;display:inline-block}.at-custom-sidebar .at-custom-sidebar-count{font-size:21px;line-height:1.25em;color:#222}.at-custom-sidebar .at-custom-sidebar-text{font-size:10px;line-height:1.25em;color:#888;letter-spacing:1px}.at-custom-sidebar .at-icon-wrapper{text-align:center;margin:0 4px}.at-custom-sidebar .at-icon{vertical-align:top;margin:9px;width:2pc;height:2pc}.at-custom-sidebar .at-icon-wrapper{position:relative}.at-custom-sidebar .at4-share-count,.at-custom-sidebar .at4-share-count-container{line-height:1pc;font-size:10px}.at-custom-sidebar .at4-share-count{text-indent:0;font-family:Arial,Helvetica Neue,Helvetica,sans-serif;font-weight:200;width:100%;height:1pc}.at-custom-sidebar .at4-share-count-anchor .at-icon{margin-top:3px}.at-custom-sidebar .at4-share-count-container{position:absolute;left:0;right:auto;top:auto;bottom:0;width:100%;color:#fff;background:inherit}</style><style type="text/css">.at-image-sharing-mobile-icon{position:absolute;background:#000 url(https://s7.addthis.com/static/44a36d35bafef33aa9455b7d3039a771.png) no-repeat top center;background-color:rgba(0,0,0,.9);background-image:url(https://s7.addthis.com/static/10db525181ee0bbe1a515001be1c7818.svg),none;border-radius:3px;width:50px;height:40px;top:-9999px;left:-9999px}.at-image-sharing-tool{display:block;position:absolute;text-align:center;z-index:9001;background:none;overflow:hidden;top:-9999px;left:-9999px;font:initial;line-height:0}.at-image-sharing-tool.addthis-animated{animation-duration:.15s}.at-image-sharing-tool.at-orientation-vertical .at-share-btn{display:block}.at-image-sharing-tool.at-orientation-horizontal .at-share-btn{display:inline-block}.at-image-sharing-tool.at-image-sharing-tool-size-big .at-icon{width:43px;height:43px}.at-image-sharing-tool.at-image-sharing-tool-size-mobile .at-share-btn{margin:0!important}.at-image-sharing-tool.at-image-sharing-tool-size-mobile .at-icon-wrapper{height:60px;width:100%;border-radius:0!important}.at-image-sharing-tool.at-image-sharing-tool-size-mobile .at-icon{max-width:100%;height:54px!important;width:54px!important}.at-image-sharing-tool .at-custom-shape.at-image-sharing-tool-btns{margin-right:8px;margin-bottom:8px}.at-image-sharing-tool .at-custom-shape .at-share-btn{margin-top:8px;margin-left:8px}.at-image-sharing-tool .at-share-btn{line-height:0;text-decoration:none;transition:none;box-sizing:content-box}.at-image-sharing-tool .at-icon-wrapper{text-align:center;height:100%;width:100%}.at-image-sharing-tool .at-icon{vertical-align:top;width:2pc;height:2pc;margin:3px}</style><style type="text/css">.at-expanding-share-button{box-sizing:border-box;position:fixed;z-index:9999}.at-expanding-share-button[data-position=bottom-right]{bottom:10px;right:10px}.at-expanding-share-button[data-position=bottom-right] .at-expanding-share-button-toggle-bg,.at-expanding-share-button[data-position=bottom-right] .at-expanding-share-button-toggle-btn[data-name]:after,.at-expanding-share-button[data-position=bottom-right] .at-icon-wrapper,.at-expanding-share-button[data-position=bottom-right] [data-name]:after{float:right}.at-expanding-share-button[data-position=bottom-right] [data-name]:after{margin-right:10px}.at-expanding-share-button[data-position=bottom-right] .at-expanding-share-button-toggle-btn[data-name]:after{margin-right:5px}.at-expanding-share-button[data-position=bottom-right] .at-icon-wrapper{margin-right:-3px}.at-expanding-share-button[data-position=bottom-left]{bottom:10px;left:10px}.at-expanding-share-button[data-position=bottom-left] .at-expanding-share-button-toggle-bg,.at-expanding-share-button[data-position=bottom-left] .at-expanding-share-button-toggle-btn[data-name]:after,.at-expanding-share-button[data-position=bottom-left] .at-icon-wrapper,.at-expanding-share-button[data-position=bottom-left] [data-name]:after{float:left}.at-expanding-share-button[data-position=bottom-left] [data-name]:after{margin-left:10px}.at-expanding-share-button[data-position=bottom-left] .at-expanding-share-button-toggle-btn[data-name]:after{margin-left:5px}.at-expanding-share-button *,.at-expanding-share-button :after,.at-expanding-share-button :before{box-sizing:border-box}.at-expanding-share-button .at-expanding-share-button-services-list{display:none;list-style:none;margin:0 5px;overflow:visible;padding:0}.at-expanding-share-button .at-expanding-share-button-services-list>li{display:block;height:45px;position:relative;overflow:visible}.at-expanding-share-button .at-expanding-share-button-toggle-btn,.at-expanding-share-button .at-share-btn{transition:.1s;text-decoration:none}.at-expanding-share-button .at-share-btn{display:block;height:40px;padding:0 3px 0 0}.at-expanding-share-button .at-expanding-share-button-toggle-btn{position:relative;overflow:auto}.at-expanding-share-button .at-expanding-share-button-toggle-btn.at-expanding-share-button-hidden[data-name]:after{display:none}.at-expanding-share-button .at-expanding-share-button-toggle-bg{box-shadow:0 2px 4px 0 rgba(0,0,0,.3);border-radius:50%;position:relative}.at-expanding-share-button .at-expanding-share-button-toggle-bg>span{background-image:url("data:image/svg+xml,%3Csvg%20width%3D%2232px%22%20height%3D%2232px%22%20viewBox%3D%220%200%2032%2032%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Ctitle%3Eshare%3C%2Ftitle%3E%3Cg%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%3Cg%20fill%3D%22%23FFFFFF%22%3E%3Cpath%20d%3D%22M26%2C13.4285714%20C26%2C13.6220248%2025.9293162%2C13.7894338%2025.7879464%2C13.9308036%20L20.0736607%2C19.6450893%20C19.932291%2C19.786459%2019.7648819%2C19.8571429%2019.5714286%2C19.8571429%20C19.3779752%2C19.8571429%2019.2105662%2C19.786459%2019.0691964%2C19.6450893%20C18.9278267%2C19.5037195%2018.8571429%2C19.3363105%2018.8571429%2C19.1428571%20L18.8571429%2C16.2857143%20L16.3571429%2C16.2857143%20C15.6279725%2C16.2857143%2014.9750773%2C16.3080355%2014.3984375%2C16.3526786%20C13.8217977%2C16.3973217%2013.2488868%2C16.477306%2012.6796875%2C16.5926339%20C12.1104882%2C16.7079619%2011.6157015%2C16.8660704%2011.1953125%2C17.0669643%20C10.7749235%2C17.2678581%2010.3824423%2C17.5264121%2010.0178571%2C17.8426339%20C9.65327199%2C18.1588557%209.35565592%2C18.534596%209.125%2C18.9698661%20C8.89434408%2C19.4051361%208.71391434%2C19.9203839%208.58370536%2C20.515625%20C8.45349637%2C21.1108661%208.38839286%2C21.7842224%208.38839286%2C22.5357143%20C8.38839286%2C22.9449425%208.40699386%2C23.4025272%208.44419643%2C23.9084821%20C8.44419643%2C23.9531252%208.45349693%2C24.0405499%208.47209821%2C24.1707589%20C8.4906995%2C24.3009679%208.5%2C24.3995532%208.5%2C24.4665179%20C8.5%2C24.5781256%208.46837829%2C24.6711306%208.40513393%2C24.7455357%20C8.34188956%2C24.8199408%208.25446484%2C24.8571429%208.14285714%2C24.8571429%20C8.02380893%2C24.8571429%207.9196433%2C24.7938994%207.83035714%2C24.6674107%20C7.77827355%2C24.6004461%207.72991094%2C24.5186017%207.68526786%2C24.421875%20C7.64062478%2C24.3251483%207.59040206%2C24.2135423%207.53459821%2C24.0870536%20C7.47879436%2C23.9605648%207.43973225%2C23.87128%207.41741071%2C23.8191964%20C6.47246551%2C21.6986501%206%2C20.0208395%206%2C18.7857143%20C6%2C17.3050521%206.19717065%2C16.0662252%206.59151786%2C15.0691964%20C7.79688103%2C12.0706695%2011.0520568%2C10.5714286%2016.3571429%2C10.5714286%20L18.8571429%2C10.5714286%20L18.8571429%2C7.71428571%20C18.8571429%2C7.52083237%2018.9278267%2C7.35342333%2019.0691964%2C7.21205357%20C19.2105662%2C7.07068382%2019.3779752%2C7%2019.5714286%2C7%20C19.7648819%2C7%2019.932291%2C7.07068382%2020.0736607%2C7.21205357%20L25.7879464%2C12.9263393%20C25.9293162%2C13.067709%2026%2C13.2351181%2026%2C13.4285714%20L26%2C13.4285714%20Z%22%3E%3C%2Fpath%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E");background-position:center center;background-repeat:no-repeat;transition:transform .4s ease;border-radius:50%;display:block}.at-expanding-share-button .at-icon-wrapper{box-shadow:0 2px 4px 0 rgba(0,0,0,.3);border-radius:50%;display:inline-block;height:40px;line-height:40px;text-align:center;width:40px}.at-expanding-share-button .at-icon{display:inline-block;height:34px;margin:3px 0;vertical-align:top;width:34px}.at-expanding-share-button [data-name]:after{box-shadow:0 2px 4px 0 rgba(0,0,0,.3);transform:translate(0, -50%);transition:.4s;background-color:#fff;border-radius:3px;color:#666;content:attr(data-name);font-family:Helvetica Neue,Helvetica,Arial,sans-serif;font-size:9pt;line-height:9pt;font-weight:500;opacity:0;padding:3px 5px;position:relative;top:20px;white-space:nowrap}.at-expanding-share-button.at-expanding-share-button-show-icons .at-expanding-share-button-services-list{display:block}.at-expanding-share-button.at-expanding-share-button-animate-in .at-expanding-share-button-toggle-bg>span{transform:rotate(270deg);background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%20viewBox%3D%220%200%2032%2032%22%3E%3Cg%3E%3Cpath%20d%3D%22M18%2014V8h-4v6H8v4h6v6h4v-6h6v-4h-6z%22%20fill-rule%3D%22evenodd%22%20fill%3D%22white%22%3E%3C%2Fpath%3E%3C%2Fg%3E%3C%2Fsvg%3E");background-position:center center;background-repeat:no-repeat}.at-expanding-share-button.at-expanding-share-button-animate-in [data-name]:after{opacity:1}.at-expanding-share-button.at-hide-label [data-name]:after{display:none}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle{height:50px}.at-expanding-share-button.at-expanding-share-button-desktop .at-icon-wrapper:hover{box-shadow:0 2px 5px 0 rgba(0,0,0,.5)}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle-bg{height:50px;line-height:50px;width:50px}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle-bg>span{height:50px;width:50px}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle-bg:after{box-shadow:0 2px 5px 0 rgba(0,0,0,.2);transition:opacity .2s ease;border-radius:50%;content:'';height:100%;opacity:0;position:absolute;top:0;left:0;width:100%}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle-bg:hover:after{opacity:1}.at-expanding-share-button.at-expanding-share-button-desktop .at-expanding-share-button-toggle-btn[data-name]:after{top:25px}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-services-list{margin:0}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-toggle-btn,.at-expanding-share-button.at-expanding-share-button-mobile .at-share-btn{outline:0}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-toggle{height:40px;-webkit-tap-highlight-color:transparent}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-toggle-bg,.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-toggle-bg span{height:40px;line-height:40px;width:40px}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-click-flash{transform:scale(0);transition:transform ease,opacity ease-in;background-color:hsla(0,0%,100%,.3);border-radius:50%;height:40px;opacity:1;position:absolute;width:40px;z-index:10000}.at-expanding-share-button.at-expanding-share-button-mobile .at-expanding-share-button-click-flash.at-expanding-share-button-click-flash-animate{transform:scale(1);opacity:0}.at-expanding-share-button.at-expanding-share-button-mobile+.at-expanding-share-button-mobile-overlay{transition:opacity ease;bottom:0;background-color:hsla(0,0%,87%,.7);display:block;height:auto;left:0;opacity:0;position:fixed;right:0;top:0;width:auto;z-index:9998}.at-expanding-share-button.at-expanding-share-button-mobile+.at-expanding-share-button-mobile-overlay.at-expanding-share-button-hidden{height:0;width:0;z-index:-10000}.at-expanding-share-button.at-expanding-share-button-mobile.at-expanding-share-button-animate-in+.at-expanding-share-button-mobile-overlay{transition:opacity ease;opacity:1}</style><style type="text/css">.at-tjin-element .at300b,.at-tjin-element .at300m{display:inline-block;width:auto;padding:0;margin:0 2px 5px;outline-offset:-1px;transition:all .2s ease-in-out}.at-tjin-element .at300b:focus,.at-tjin-element .at300b:hover,.at-tjin-element .at300m:focus,.at-tjin-element .at300m:hover{transform:translateY(-4px)}.at-tjin-element .addthis_tjin_label{display:none}.at-tjin-element .addthis_vertical_style .at300b,.at-tjin-element .addthis_vertical_style .at300m{display:block}.at-tjin-element .addthis_vertical_style .at300b .addthis_tjin_label,.at-tjin-element .addthis_vertical_style .at300b .at-icon-wrapper,.at-tjin-element .addthis_vertical_style .at300m .addthis_tjin_label,.at-tjin-element .addthis_vertical_style .at300m .at-icon-wrapper{display:inline-block;vertical-align:middle;margin-right:5px}.at-tjin-element .addthis_vertical_style .at300b:focus,.at-tjin-element .addthis_vertical_style .at300b:hover,.at-tjin-element .addthis_vertical_style .at300m:focus,.at-tjin-element .addthis_vertical_style .at300m:hover{transform:none}.at-tjin-element .at-tjin-btn{margin:0 5px 5px 0;padding:0;outline-offset:-1px;display:inline-block;box-sizing:content-box;transition:all .2s ease-in-out}.at-tjin-element .at-tjin-btn:focus,.at-tjin-element .at-tjin-btn:hover{transform:translateY(-4px)}.at-tjin-element .at-tjin-title{margin:0 0 15px}</style><style type="text/css">#addthissmartlayerscssready{color:#bada55!important}.addthis-smartlayers,div#at4-follow,div#at4-share,div#at4-thankyou,div#at4-whatsnext{padding:0;margin:0}#at4-follow-label,#at4-share-label,#at4-whatsnext-label,.at4-recommended-label.hidden{padding:0;border:none;background:none;position:absolute;top:0;left:0;height:0;width:0;overflow:hidden;text-indent:-9999em}.addthis-smartlayers .at4-arrow:hover{cursor:pointer}.addthis-smartlayers .at4-arrow:after,.addthis-smartlayers .at4-arrow:before{content:none}a.at4-logo{background:url(data:image/gif;base64,R0lGODlhBwAHAJEAAP9uQf///wAAAAAAACH5BAkKAAIALAAAAAAHAAcAAAILFH6Ge8EBH2MKiQIAOw==) no-repeat left center}.at4-minimal a.at4-logo{background:url(data:image/gif;base64,R0lGODlhBwAHAJEAAP9uQf///wAAAAAAACH5BAkKAAIALAAAAAAHAAcAAAILFH6Ge8EBH2MKiQIAOw==) no-repeat left center!important}button.at4-closebutton{position:absolute;top:0;right:0;padding:0;margin-right:10px;cursor:pointer;background:transparent;border:0;-webkit-appearance:none;font-size:19px;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.2}button.at4-closebutton:hover{color:#000;text-decoration:none;cursor:pointer;opacity:.5}div.at4-arrow{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAoCAYAAABpYH0BAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAV1JREFUeNrsmesOgyAMhQfxwfrofTM3E10ME2i5Oeppwr9a5OMUCrh1XV+wcvNAAIAA+BiAzrmtUWln27dbjEcC3AdODfo0BdEPhmcO4nIDvDNELi2jggk4/k8dT7skfeKzWIEd4VUpMQKvNB7X+OZSmAZkATWC1xvipbpnLmOosbJZC08CkAeA4E6qFUEMwLAGnlSBPCE8lW8CYnZTcimH2HoT7kSFOx5HBmCnDhTIu1p5s98G+QZrxGPhZVMY1vgyAQaAAAiAAAgDQACcBOD+BvJtBWfRy7NpJK5tBe4FNzXokywV734wPHMQlxvgnSGyNoUP/2ACjv/7iSeYKO3YWKzAjvCqlBiBVxqPa3ynexNJwOsN8TJbzL6JNIYYXWpMv4lIIAZgWANPqkCeEJ7KNwExu8lpLlSpAVQarO77TyKdBsyRPuwV0h0gmoGnTWFYzVkYBoAA+I/2FmAAt6+b5XM9mFkAAAAASUVORK5CYII=);background-repeat:no-repeat;width:20px;height:20px;margin:0;padding:0;overflow:hidden;text-indent:-9999em;text-align:left;cursor:pointer}#at4-recommendedpanel-outer-container .at4-arrow.at-right,div.at4-arrow.at-right{background-position:-20px 0}#at4-recommendedpanel-outer-container .at4-arrow.at-left,div.at4-arrow.at-left{background-position:0 0}div.at4-arrow.at-down{background-position:-60px 0}div.at4-arrow.at-up{background-position:-40px 0}.ats-dark div.at4-arrow.at-right{background-position:-20px -20px}.ats-dark div.at4-arrow.at-left{background-position:0 -20px}.ats-dark div.at4-arrow.at-down{background-position:-60px -20px}.ats-dark div.at4-arrow.at-up{background-position:-40px -20}.at4-opacity-hidden{opacity:0!important}.at4-opacity-visible{opacity:1!important}.at4-visually-hidden{position:absolute;clip:rect(1px,1px,1px,1px);padding:0;border:0;overflow:hidden}.at4-hidden-off-screen,.at4-hidden-off-screen *{position:absolute!important;top:-9999px!important;left:-9999px!important}.at4-show{display:block!important;opacity:1!important}.at4-show-content{opacity:1!important;visibility:visible}.at4-hide{display:none!important;opacity:0!important}.at4-hide-content{opacity:0!important;visibility:hidden}.at4-visible{display:block!important;opacity:0!important}.at-wordpress-hide{display:none!important;opacity:0!important}.addthis-animated{animation-fill-mode:both;animation-timing-function:ease-out;animation-duration:.3s}.slideInDown.addthis-animated,.slideInLeft.addthis-animated,.slideInRight.addthis-animated,.slideInUp.addthis-animated,.slideOutDown.addthis-animated,.slideOutLeft.addthis-animated,.slideOutRight.addthis-animated,.slideOutUp.addthis-animated{animation-duration:.4s}@keyframes fadeIn{0%{opacity:0}to{opacity:1}}.fadeIn{animation-name:fadeIn}@keyframes fadeInUp{0%{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}.fadeInUp{animation-name:fadeInUp}@keyframes fadeInDown{0%{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}.fadeInDown{animation-name:fadeInDown}@keyframes fadeInLeft{0%{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:translateX(0)}}.fadeInLeft{animation-name:fadeInLeft}@keyframes fadeInRight{0%{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}.fadeInRight{animation-name:fadeInRight}@keyframes fadeOut{0%{opacity:1}to{opacity:0}}.fadeOut{animation-name:fadeOut}@keyframes fadeOutUp{0%{opacity:1;transform:translateY(0)}to{opacity:0;transform:translateY(-20px)}}.fadeOutUp{animation-name:fadeOutUp}@keyframes fadeOutDown{0%{opacity:1;transform:translateY(0)}to{opacity:0;transform:translateY(20px)}}.fadeOutDown{animation-name:fadeOutDown}@keyframes fadeOutLeft{0%{opacity:1;transform:translateX(0)}to{opacity:0;transform:translateX(-20px)}}.fadeOutLeft{animation-name:fadeOutLeft}@keyframes fadeOutRight{0%{opacity:1;transform:translateX(0)}to{opacity:0;transform:translateX(20px)}}.fadeOutRight{animation-name:fadeOutRight}@keyframes slideInUp{0%{transform:translateY(1500px)}0%,to{opacity:1}to{transform:translateY(0)}}.slideInUp{animation-name:slideInUp}.slideInUp.addthis-animated{animation-duration:.4s}@keyframes slideInDown{0%{transform:translateY(-850px)}0%,to{opacity:1}to{transform:translateY(0)}}.slideInDown{animation-name:slideInDown}@keyframes slideOutUp{0%{transform:translateY(0)}0%,to{opacity:1}to{transform:translateY(-250px)}}.slideOutUp{animation-name:slideOutUp}@keyframes slideOutUpFast{0%{transform:translateY(0)}0%,to{opacity:1}to{transform:translateY(-1250px)}}#at4m-menu.slideOutUp{animation-name:slideOutUpFast}@keyframes slideOutDown{0%{transform:translateY(0)}0%,to{opacity:1}to{transform:translateY(350px)}}.slideOutDown{animation-name:slideOutDown}@keyframes slideOutDownFast{0%{transform:translateY(0)}0%,to{opacity:1}to{transform:translateY(1250px)}}#at4m-menu.slideOutDown{animation-name:slideOutDownFast}@keyframes slideInLeft{0%{opacity:0;transform:translateX(-850px)}to{transform:translateX(0)}}.slideInLeft{animation-name:slideInLeft}@keyframes slideInRight{0%{opacity:0;transform:translateX(1250px)}to{transform:translateX(0)}}.slideInRight{animation-name:slideInRight}@keyframes slideOutLeft{0%{transform:translateX(0)}to{opacity:0;transform:translateX(-350px)}}.slideOutLeft{animation-name:slideOutLeft}@keyframes slideOutRight{0%{transform:translateX(0)}to{opacity:0;transform:translateX(350px)}}.slideOutRight{animation-name:slideOutRight}.at4win{margin:0 auto;background:#fff;border:1px solid #ebeced;width:25pc;box-shadow:0 0 10px rgba(0,0,0,.3);border-radius:8px;font-family:helvetica neue,helvetica,arial,sans-serif;text-align:left;z-index:9999}.at4win .at4win-header{position:relative;border-bottom:1px solid #f2f2f2;background:#fff;height:49px;-webkit-border-top-left-radius:8px;-webkit-border-top-right-radius:8px;-moz-border-radius-topleft:8px;-moz-border-radius-topright:8px;border-top-left-radius:8px;border-top-right-radius:8px;cursor:default}.at4win .at4win-header .at-h3,.at4win .at4win-header h3{height:49px;line-height:49px;margin:0 50px 0 0;padding:1px 0 0;margin-left:20px;font-family:helvetica neue,helvetica,arial,sans-serif;font-size:1pc;font-weight:700;text-shadow:0 1px #fff;color:#333}.at4win .at4win-header .at-h3 img,.at4win .at4win-header h3 img{display:inline-block;margin-right:4px}.at4win .at4win-header .at4-close{display:block;position:absolute;top:0;right:0;background:url("data:image/gif;base64,R0lGODlhFAAUAIABAAAAAP///yH5BAEAAAEALAAAAAAUABQAAAIzBIKpG+YMm5Enpodw1HlCfnkKOIqU1VXk55goVb2hi7Y0q95lfG70uurNaqLgTviyyUoFADs=") no-repeat center center;background-repeat:no-repeat;background-position:center center;border-left:1px solid #d2d2d1;width:49px;height:49px;line-height:49px;overflow:hidden;text-indent:-9999px;text-shadow:none;cursor:pointer;opacity:.5;border:0;transition:opacity .15s ease-in}.at4win .at4win-header .at4-close::-moz-focus-inner{border:0;padding:0}.at4win .at4win-header .at4-close:hover{opacity:1;background-color:#ebeced;border-top-right-radius:7px}.at4win .at4win-content{position:relative;background:#fff;min-height:220px}#at4win-footer{position:relative;background:#fff;border-top:1px solid #d2d2d1;-webkit-border-bottom-right-radius:8px;-webkit-border-bottom-left-radius:8px;-moz-border-radius-bottomright:8px;-moz-border-radius-bottomleft:8px;border-bottom-right-radius:8px;border-bottom-left-radius:8px;height:11px;line-height:11px;padding:5px 20px;font-size:11px;color:#666;-ms-box-sizing:content-box;-o-box-sizing:content-box;box-sizing:content-box}#at4win-footer a{margin-right:10px;text-decoration:none;color:#666}#at4win-footer a:hover{text-decoration:none;color:#000}#at4win-footer a.at4-logo{top:5px;padding-left:10px}#at4win-footer a.at4-privacy{position:absolute;top:5px;right:10px;padding-right:14px}.at4win.ats-dark{border-color:#555;box-shadow:none}.at4win.ats-dark .at4win-header{background:#1b1b1b;-webkit-border-top-left-radius:6px;-webkit-border-top-right-radius:6px;-moz-border-radius-topleft:6px;-moz-border-radius-topright:6px;border-top-left-radius:6px;border-top-right-radius:6px}.at4win.ats-dark .at4win-header .at4-close{background:url("data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAAWdEVYdENyZWF0aW9uIFRpbWUAMTEvMTMvMTKswDp5AAAAd0lEQVQ4jb2VQRLAIAgDE///Z3qqY1FAhalHMCsCIkVEAIAkkVgvp2lDBgYAnAyHkWotLccNrEd4A7X2TqIdqLfnWBAdaF5rJdyJfjtPH5GT37CaGhoVq3nOm/XflUuLUto2pY1d+vRKh0Pp+MrAVtDe2JkvYNQ+jVSEEFmOkggAAAAASUVORK5CYII=") no-repeat center center;background-image:url(https://s7.addthis.com/static/fb08f6d50887bd0caacc86a62bcdcf68.svg),none;border-color:#333}.at4win.ats-dark .at4win-header .at4-close:hover{background-color:#000}.at4win.ats-dark .at4win-header .at-h3,.at4win.ats-dark .at4win-header h3{color:#fff;text-shadow:0 1px #000}.at4win.ats-gray .at4win-header{background:#fff;border-color:#d2d2d1;-webkit-border-top-left-radius:6px;-webkit-border-top-right-radius:6px;-moz-border-radius-topleft:6px;-moz-border-radius-topright:6px;border-top-left-radius:6px;border-top-right-radius:6px}.at4win.ats-gray .at4win-header a.at4-close{border-color:#d2d2d1}.at4win.ats-gray .at4win-header a.at4-close:hover{background-color:#ebeced}.at4win.ats-gray #at4win-footer{border-color:#ebeced}.at4win .clear{clear:both}.at4win ::selection{background:#fe6d4c;color:#fff}.at4win ::-moz-selection{background:#fe6d4c;color:#fff}.at4-icon-fw{display:inline-block;background-repeat:no-repeat;background-position:0 0;margin:0 5px 0 0;overflow:hidden;text-indent:-9999em;cursor:pointer;padding:0;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%}.at44-follow-container a.aticon{height:2pc;margin:0 5px 5px 0}.at44-follow-container .at4-icon-fw{margin:0}</style><script async="" type="text/javascript" src="./fibonacci_files/gpt.js.download" dropped-by="bsaoptimize"></script><meta http-equiv="origin-trial" content="Az6AfRvI8mo7yiW5fLfj04W21t0ig6aMsGYpIqMTaX60H+b0DkO1uDr+7BrzMcimWzv/X7SXR8jI+uvbV0IJlwYAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A+USTya+tNvDPaxUgJooz+LaVk5hPoAxpLvSxjogX4Mk8awCTQ9iop6zJ9d5ldgU7WmHqBlnQB41LHHRFxoaBwoAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7FovoGr67TUBYbnY+Z0IKoJbbmRmB8fCyirUGHavNDtD91CiGyHHSA2hDG9r9T3NjUKFi6egL3RbgTwhhcVDwUAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script src="./fibonacci_files/pubads_impl_2022111501.js.download" async=""></script><style id="bsa_extra-css"></style><meta http-equiv="origin-trial" content="A/vXSuiuvzsL+Db89QNS/YzqK5Wmzx9oASGHZVMjcaWfVdbB6eUJrJGNr7uhrsmiGhryVjVALd72agYzELDTMAgAAACAeyJvcmlnaW4iOiJodHRwczovL2NyaXRlby5uZXQ6NDQzIiwiZmVhdHVyZSI6IlByaXZhY3lTYW5kYm94QWRzQVBJcyIsImV4cGlyeSI6MTY2OTc2NjM5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><meta http-equiv="origin-trial" content="A0KGawWMfAygakxUO+Z3rulPwK2j0AqkLneiEt4pAI951GYaafeHNV9Ya+PAn7s0y12QSrfTjc9LdOUU+QfkdQwAAACAeyJvcmlnaW4iOiJodHRwczovL2NyaXRlby5jb206NDQzIiwiZmVhdHVyZSI6IlByaXZhY3lTYW5kYm94QWRzQVBJcyIsImV4cGlyeSI6MTY2OTc2NjM5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><script src="./fibonacci_files/mode-python.js.download"></script><link rel="preload" href="./fibonacci_files/f.txt" as="script"><script type="text/javascript" src="./fibonacci_files/f.txt"></script><link rel="preload" href="./fibonacci_files/f(1).txt" as="script"><script type="text/javascript" src="./fibonacci_files/f(1).txt"></script><script src="./fibonacci_files/python.js.download"></script></head>

<body class="">
        <span id="mobile_test_element"></span>
    <div class="container" style="width:100%;padding:0px;margin:0px">

    <div class="col-sm-12" style="margin:0px;padding:0px">
        <div style="height:100vh">
<div class="split-pane fixed-left" style="min-width: 2px;">
    <div class="split-pane-component " id="left-component" style="background-color: #125792;">
        <div style="background-color: #125792; padding:10px 0px 0px 0px">
          
          <a id="btn_close_header" onclick="fold_left_bar();"><span class="glyphicon glyphicon-menu-left" aria-hidden="true" style="z-index:100;background-color:#0f3a5f;padding:20px 0px;"></span>
          
          </a><h4 id="header_logo" style="width:100%;text-align:center;margin:0px; border-bottom: 0px solid #94c5ee; padding-bottom: 0px;"><a id="btn_close_header" onclick="fold_left_bar();">
            </a><a href="https://www.onlinegdb.com/">
              <span class="glyphicon glyphicon-flash" style="padding: 5px; border: 3px solid;" aria-hidden="true"></span> 
              <span class="to_be_hidden">
          &nbsp;&nbsp;OnlineGDB <sup> beta</sup>
          </span>
          </a>
          </h4>
          
          <span class="tagline to_be_hidden">
              <h1 style="font-size:12px;padding:0px; margin:0px">
                  
                  online compiler and debugger for c/c++
                  
                </h1>
        </span>
          </div>
          <div class="to_be_hidden">
          <div style="text-align: center;    color: #ccd7dd;    padding: 10px 0px;    font-style: italic;    border-top: 1px solid #658a9e;    border-bottom: 1px solid #658a9e;">
              
              code. compile. run. debug. share.
              
          </div>
          
          <ul class="nav nav-tabs nav-stacked text-center" style="background-color: #337ab7; border-bottom:1px solid #658a9e">
                
                <li id="navbar_project_title">fibonacci.py</li><li><a href="https://www.onlinegdb.com/">Create New Project</a></li>
                
                <li><a href="https://www.onlinegdb.com/myfiles">My Projects</a></li>
                
                <!--<li ><a href="/s/">Student</a></li>-->
                <li><a href="https://www.onlinegdb.com/classroom">Classroom <span class="label label-danger">new</span></a></li>
                
                <li><a href="https://learn.onlinegdb.com/">Learn Programming</a></li>
                <li><a href="https://question.onlinegdb.com/">Programming Questions</a></li>
                
                
<!--
                <li ><a href="/opportunity">Opportunity for Intern <span class="label label-danger">new</span></a></li>
-->
<!--                <li ><a href="/career">We are Hiring</a></li> -->
                
                <!--
                <li ><a href="/career">Jobs <span class="label label-danger">new</span></a></li>
                -->
                
                <li><a href="https://www.onlinegdb.com/register">Sign Up</a></li>
                <li id="login_logout_span"><a href="https://www.onlinegdb.com/logout">Logout</a></li>
                
          </ul>
        <div class="addthis_inline_share_toolbox" data-url="https://www.onlinegdb.com/" data-title="GDB online Debugger | Compiler - Code, Compile, Run, Debug online C, C++" data-description="Online GDB is online compiler and debugger for C/C++. You can compile, run and debug code with gdb online. Using gcc/g++ as compiler and gdb as debugger. Currently C and C++ languages are supported." style="clear: both;"><div id="atstbx" class="at-resp-share-element at-style-responsive addthis-smartlayers addthis-animated at4-show" aria-labelledby="at-99536df0-feb6-4537-9829-a98388aa3798" role="region"><span id="at-99536df0-feb6-4537-9829-a98388aa3798" class="at4-visually-hidden">AddThis Sharing Buttons</span><div class="at-share-btn-elements"><a role="button" tabindex="0" class="at-icon-wrapper at-share-btn at-svc-facebook" style="background-color: rgb(59, 89, 152); border-radius: 0px;"><span class="at4-visually-hidden">Share to Facebook</span><span class="at-icon-wrapper" style="line-height: 32px; height: 32px; width: 32px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32" version="1.1" role="img" aria-labelledby="at-svg-facebook-1" class="at-icon at-icon-facebook" style="fill: rgb(255, 255, 255); width: 32px; height: 32px;"><title id="at-svg-facebook-1">Facebook</title><g><path d="M22 5.16c-.406-.054-1.806-.16-3.43-.16-3.4 0-5.733 1.825-5.733 5.17v2.882H9v3.913h3.837V27h4.604V16.965h3.823l.587-3.913h-4.41v-2.5c0-1.123.347-1.903 2.198-1.903H22V5.16z" fill-rule="evenodd"></path></g></svg></span></a><a role="button" tabindex="0" class="at-icon-wrapper at-share-btn at-svc-twitter" style="background-color: rgb(29, 161, 242); border-radius: 0px;"><span class="at4-visually-hidden">Share to Twitter</span><span class="at-icon-wrapper" style="line-height: 32px; height: 32px; width: 32px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32" version="1.1" role="img" aria-labelledby="at-svg-twitter-2" class="at-icon at-icon-twitter" style="fill: rgb(255, 255, 255); width: 32px; height: 32px;"><title id="at-svg-twitter-2">Twitter</title><g><path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path></g></svg></span></a><a role="button" tabindex="0" class="at-icon-wrapper at-share-btn at-svc-compact" style="background-color: rgb(255, 101, 80); border-radius: 0px;"><span class="at4-visually-hidden">Share to More</span><span class="at-icon-wrapper" style="line-height: 32px; height: 32px; width: 32px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32" version="1.1" role="img" aria-labelledby="at-svg-addthis-3" class="at-icon at-icon-addthis" style="fill: rgb(255, 255, 255); width: 32px; height: 32px;"><title id="at-svg-addthis-3">AddThis</title><g><path d="M18 14V8h-4v6H8v4h6v6h4v-6h6v-4h-6z" fill-rule="evenodd"></path></g></svg></span><span class="at4-share-count-container" style="font-size: 11.4px; line-height: 32px; color: rgb(255, 255, 255);">187K</span></a></div></div></div>
        
        <!--
        <center>
        <script src="https://donorbox.org/install-popup-button.js" type="text/javascript" defer></script>
<a class="dbox-donation-button" href="https://donorbox.org/donate-to-onlinegdb" style="background:#5cb85c url(https://d1iczxrky3cnb2.cloudfront.net/white_logo.png) no-repeat 18px center; color: #fff;text-decoration: none;font-family: Verdana,sans-serif;display: inline-block;font-size: 14px;padding: 6px 17px 6px 56px; -webkit-border-radius: 2px; -moz-border-radius: 2px; border-radius: 2px; box-shadow: 0 1px 0 0 #408040; text-shadow: 0 1px rgba(0, 0, 0, 0.3);" >Donate</a>
</center> -->
<center>
    <div id="ad_wrapper">
    
    
    
    <script type="text/javascript">var do_fallback_ad_check = true;</script>
    
    
    <script type="text/javascript">var no_ads = false; </script>
    
    <script async="" type="text/javascript" src="./fibonacci_files/carbon.js.download" id="_carbonads_js"></script><div id="carbonads"><span><span class="carbon-wrap"><a href="https://tracking.vcommission.com/aff_c?offer_id=8231&amp;aff_id=66738" class="carbon-img" target="_blank" rel="noopener sponsored"><img src="./fibonacci_files/1534850820-rakuten.jpg" alt="ads via Carbon" border="0" height="100" width="130" style="max-width: 130px;"></a><a href="https://tracking.vcommission.com/aff_c?offer_id=8231&amp;aff_id=66738" class="carbon-text" target="_blank" rel="noopener sponsored">Have fun taking surveys and get paid!</a></span><a href="http://carbonads.net/?utm_source=onlinegdbcom&amp;utm_medium=ad_via_link&amp;utm_campaign=in_unit&amp;utm_term=carbon" class="carbon-poweredby" target="_blank" rel="noopener sponsored">ads via Carbon</a></span></div> 
    
    </div>
</center>
        
        <footer class="container-fluid text-center" style="bottom:0px;left:0px;right:0px;position:absolute;padding:3px;">
        <style type="text/css">
#footer a {
    font-weight: normal;
    text-decoration: none;
}
#footer a:hover {
    color:white;
    text-decoration: underline;
}
</style>
<div id="footer">
    <span class="text-center" style="font-weight:normal; border-bottom:1px solid #658a9e">
        <a href="https://www.onlinegdb.com/about">About</a>
        • <a href="https://www.onlinegdb.com/faq">FAQ</a>
        • <a href="https://www.onlinegdb.com/blog/">Blog</a>
        <!--<li ><a href="/contact?cat=feature" >Feature Request</a></li>-->
        <!--<li ><a href="/contact?cat=bug" >Report Bug</a></li> -->
        • <a href="https://www.onlinegdb.com/termsofuse">Terms of Use</a> 
        • <a href="https://www.onlinegdb.com/contact">Contact Us</a>
        • <a href="http://www.gdbtutorial.com/" target="_blank">GDB Tutorial</a>
        • <a href="https://www.onlinegdb.com/credits"> Credits </a></span>
        • <a href="https://www.onlinegdb.com/privacy"> Privacy </a>
    <div style="clear:both"></div>
        <!--<li><a href="http://www.whizcoder.com/" target='_blank' >Online Java/Python Debugger</a></li>-->
    
<span style="float:none;clear:both">© 2016 - 2022 GDB Online</span>
</div>
        </footer>
        
        </div>
    </div>
    <div class="split-pane-divider hide" id="my-divider" style=""><div class="split-pane-divider-inner"></div></div>
    <div class="split-pane-component" id="right-component">

        <script src="./fibonacci_files/js-dos.js.download"></script>
        
        <input type="hidden" id="snippet_id" value="">
        <input type="hidden" id="sub_user_id" value="">


        <div class="split-pane fixed-left" style="min-width: 1px;">
            <div class="split-pane-component" id="right-left-component" style="width: 1171px;">
                <div class="split-pane fixed-top" style="min-height: 7px;">
                    <div class="split-pane-component" id="top-component">
                        <!-- middle top start --> 
                        <div id="native-inline"></div>
                        <div id="editor-container">
                            
    <a name="title-bar"></a>
    <div id="title-bar" style="padding:0px 5px;min-width:900px">
        <div id="connectingMessage" class="loadingdots" style="display:none">connecting to server </div>
        <div style="position:relative">
            <!--<span class="col-sm-3" style="float:left"><b>Source Code</b></span>-->
            <span class="col-sm-63" id="control-bar" style="float:left">
                
                <span id="project_title" class="hide">fibonacci.py</span>
                
                
                
                <div class="btn-group">
                <button type="button" id="control-btn-newfile" class="btn btn-default btn-half" data-placement="right" data-toggle="tooltip" title="" data-original-title="New File (Ctrl+M)"><span class="glyphicon glyphicon-file"></span></button>
                <button type="button" id="control-btn-upload" class="btn btn-default btn-half" data-placement="bottom" data-toggle="tooltip" title="" data-original-title="Upload File"><span class="glyphicon glyphicon-cloud-upload"></span></button>
                </div>

                <span id="upload_file_container" class="hide"></span>
                
                <button type="submit" id="control-btn-run" class="btn btn-success" onclick="ide.runcode();" data-placement="bottom" data-toggle="tooltip" title="" data-original-title="F9">
                    <span class="glyphicon glyphicon-play" aria-hidden="true"></span> Run</button>
                
                <button type="submit" id="control-btn-debug" class="btn btn-primary" onclick="ide.debugcode();" data-placement="bottom" data-toggle="tooltip" title="" data-original-title="F8">
                    <span class="glyphicon glyphicon-play-circle" aria-hidden="true"></span> Debug</button>
                <button type="submit" id="control-btn-stop" class="btn btn-danger" onclick="pstop(); " disabled="disabled">   <span class="glyphicon glyphicon-stop" aria-hidden="true"></span> Stop</button>
                <!--<button type="submit" id="control-btn-save" class="btn btn-warning" onclick="idesave(editor.getValue())"> <span class="glyphicon glyphicon-floppy-save" aria-hidden="true"></span> Save</button>-->
                
                
                <button type="submit" id="control-btn-share" class="btn btn-warning" onclick="shareCode()"> <span class="glyphicon glyphicon-share" aria-hidden="true"></span> Share</button>
                
                
                <button type="button" id="control-btn-save" class="btn btn-primary" data-placement="bottom" data-toggle="tooltip" title="" data-original-title="Ctrl+S" disabled="disabled"> <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span> <span class="btn_text">Saved</span></button>
                
                
                
                <button type="submit" id="control-btn-beautify" class="btn btn-info" onclick="beautifyCode()" data-placement="bottom" data-toggle="tooltip" title="" data-original-title="Ctrl+B">{ } Beautify</button>
                
                
                <button type="button" id="control-btn-download" class="btn btn-info" onclick="downloadCode()" title="" data-placement="bottom" data-toggle="tooltip" data-original-title="Download Code"><span class="glyphicon glyphicon-save" aria-hidden="true"></span></button>
                


                
                
                
                
            </span>
            

            
            <span class="col-sm-64">
                
                    <span class="" style="float:right;padding-right:50px;">
                
                Language
                <select id="lang-select" class="form-control" style="width:90px; display:inline; border-radius:0px;">
                        
                  <option disabled="" selected="" value=""> -- select -- </option>
                  <option value="c">C</option>
<!--                  <option  value="c99">C99</option>-->
                  <option value="c++">C++</option>
<!--                  <option  value="c++11">C++ 11</option> -->
                  <option value="c++14">C++ 14</option>
                  <option value="c++17">C++ 17</option>
                  <option value="c++20">C++ 20</option>
                  
                  <option value="c_tc">C (TurboC)</option>
                  <option value="c++_tc">C++ (TurboC)</option>
                  
                  <option value="java">Java</option>
                  <option value="python">Python 3</option>
                  <option value="php">PHP</option>
                  <option value="c#">C#</option>
                  <option value="ocaml">OCaml</option>
                  <option value="vb">VB</option>
                  <option value="html">HTML,JS,CSS</option>
                  <option value="ruby">Ruby</option>
                  <option value="perl">Perl</option>
                  <option value="pascal">Pascal</option>
                  <option value="r">R</option>
                  <option value="fortran">Fortran</option>
                  <option value="haskell">Haskell</option>
                  <option value="asm_gcc">Assembly(GCC)</option>
                  <option value="objc">Objective C</option>
                  <option value="sqlite3">SQLite</option>
                  <option value="js_rhino">Javascript(Rhino)</option>
                  <option value="prolog">Prolog</option>
                  <option value="swift">Swift</option>
                  
                  <option value="rust">Rust</option>
                  <option value="go">Go</option>
                  
                  <option value="bash">Bash</option> 
                </select>
                
                <button type="submit" class="btn btn-warning" onclick="ide.showinfo();">
                    <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></button>
                <button type="submit" class="btn btn-warning" onclick="ide.showsettings();">
                <span class="glyphicon glyphicon-cog" aria-hidden="true"></span></button>
                
                </span>
            </span>
            <div id="popup-settings" style="position:absolute; right:0px; z-index:123;">
                <div>
                    <button type="submit" style="visibility: hidden;" class="btn btn-warning" onclick=""> <span class="glyphicon glyphicon-cog" aria-hidden="true"></span></button>
                </div>
                <div style="background-color:#f0ad4e;padding: 15px;">
                    <p>
                        </p><form class="form-inline" role="form">
                            <div class="form-group">
                                <label for="settings-editor-theme">Editor Theme:</label>
                                <select class="form-control" id="settings-editor-theme">
                                    <option value="dark">Dark</option>
                                    <option value="light">Light</option>
                                </select>
                            </div>
                        </form>

                    <p>
                        </p><form class="form-inline" role="form">
                            <div class="form-group">
                                <label for="settings-editor-mode">Editor Mode:</label>
                                <select class="form-control" id="settings-editor-mode">
                                    <option value="textinput">Normal</option>
                                    <option value="emacs">Emacs</option>
                                    <option value="vim">vim</option>
                                </select>
                            </div>
                        </form>

                    <p>
                        </p><form class="form-inline" role="form">
                            <div class="form-group">
                                <label for="settings-editor-font-size">Font size:</label>
                                <select class="form-control" id="settings-editor-font-size">
                                    <option value="small">Small</option>
                                    <option value="medium" selected="selected">Medium</option>
                                    <option value="large">Large</option>
                                </select>
                            </div>
                        </form>

                    <p>
                        </p><form class="form-inline" role="form">
                            <div class="form-group">
                                <label for="settings-editor-tab-space">Tab Space:</label>
                                <select class="form-control" id="settings-editor-tab-space">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4" selected="selected">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                    <option value="8">8</option>
                                </select>
                            </div>
                        </form>
                    <p>
                        </p><form class="form-nline" role="form">
                            <div class="form-group">
                                <div class="input-group">
                                <label for="setting-editor-autocomplete">Autocomplete: </label>
                                <input type="radio" name="settings-editor-autocomplete" id="settings-editor-autocomplete-on" checked="">on
                                <input type="radio" name="settings-editor-autocomplete" id="settings-editor-autocomplete-off">off
                                </div>
                            </div>
                        </form>
                    <p></p>
                    <p>
                        </p><form class="form-inline" role="form">
                            <div class="form-group">
                                <button type="button" class="btn btn-primary" style="width:100%;" onclick="display_compiler_flags_box()">Extra Compiler Flags</button> 
                            </div>
                        </form>
        
                    <div>
                        <p>
                        </p><form role="form" post="#">
                            <button type="button" class="btn btn-default" style="width:100%;" onclick="ide.closesettings();">Done</button>
                        </form>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
    <div id="multi_editor_container">
        <div style="clear:both; background-color:#757575;">
            <ul class="editor_file_tabs nav nav-pills">
                
                    <li class="active">
                        <a href="https://www.onlinegdb.com/#editor_1" data-toggle="tab"><span class="filename">main.py</span>                   
                        </a>
                    </li>
                
            </ul>
        </div>
        <div class="editor_text_panes tab-content clearfix">
            
            
            <div id="editor_1" data-format="S" data-readonly-ranges="" class="tab-pane active editor ace_editor ace-idle-fingers ace_dark" style="position: absolute; width: 100%; top: 52px; bottom: 0px; font-size: medium;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 171px; left: 257px;"></textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 51px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 51px;"><div class="ace_gutter-cell " style="height: 19px; top: 0px;">1<span class="ace_fold-widget ace_start ace_open" style="display: inline-block; height: 19px;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 19px;">2<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 38px;">3<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 57px;">4<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 76px;">5<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 95px;">6<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 114px;">7<span style="display: inline-block; height: 19px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 133px;">8<span style="display: none;"></span></div><div class="ace_gutter-cell ace_gutter-active-line " style="height: 19px; top: 152px;">9<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 19px; top: 171px;">10<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 19px; left: 50.5938px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 1120.41px; height: 527px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 708px; visibility: visible;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 19px; top: 152px; left: 0px; right: 0px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 19px; width: 8.79688px; top: 152px; left: 197.531px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 19px; width: 8.79688px; top: 152px; left: 83.1719px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line" style="height: 19px; top: 0px;"><span class="ace_keyword">def</span> <span class="ace_entity ace_name ace_function">fibonacci</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">n</span><span class="ace_paren ace_rparen">)</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 19px; top: 19px;">    <span class="ace_keyword">if</span> <span class="ace_identifier">n</span> <span class="ace_keyword ace_operator">&lt;=</span> <span class="ace_constant ace_numeric">1</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 19px; top: 38px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">n</span></div><div class="ace_line" style="height: 19px; top: 57px;">    <span class="ace_keyword">return</span> <span class="ace_identifier">fibonacci</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">n</span><span class="ace_keyword ace_operator">-</span><span class="ace_constant ace_numeric">1</span><span class="ace_paren ace_rparen">)</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_identifier">fibonacci</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">n</span><span class="ace_keyword ace_operator">-</span><span class="ace_constant ace_numeric">2</span><span class="ace_paren ace_rparen">)</span></div><div class="ace_line" style="height: 19px; top: 76px;"> </div><div class="ace_line" style="height: 19px; top: 95px;"> </div><div class="ace_line" style="height: 19px; top: 114px;"><span class="ace_keyword">if</span> <span class="ace_identifier">__name__</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_string">"__main__"</span><span class="ace_punctuation">:</span></div><div class="ace_line" style="height: 19px; top: 133px;">    <span class="ace_identifier">n</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_numeric">9</span></div><div class="ace_line" style="height: 19px; top: 152px;">    <span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">fibonacci</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">n</span><span class="ace_paren ace_rparen">))</span></div><div class="ace_line" style="height: 19px; top: 171px;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 152px; left: 206px; width: 9px; height: 19px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 24px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 24px; height: 190px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 24px; left: 50.5938px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 24px; width: 1120px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
            
        </div>
    </div>
</div>
                        <!-- middle top end -->
                    </div>
                    <div class="split-pane-divider" id="my-divider1"><div class="split-pane-divider-inner"></div></div>
                    <div class="split-pane-component" id="bottom-component">
                        <button onclick="toggle_bottom_pane_size()">
                            <span class="btn_minmax glyphicon glyphicon-resize-full" title="Maximize"></span> 
                        </button>       
                        <button onclick="toggle_bottom_pane_size_hide()">
                            <span class="btn_hide glyphicon glyphicon-chevron-down" title="Hide"></span> 
                        </button> 
                        <button onclick="copy_output()">
                            <span class="btn_copy glyphicon glyphicon-copy" title="Copy output to clipboard" style="display: inline;"></span> 
                        </button>               
                        <!-- middle bottom start -->
                         <div id="console-wrapper" style="">
    <div id="console-fadder">
        <center><img src="./fibonacci_files/loading.gif"><img>
        <div class="msg-wrapper"><h4 class="msg">Compiling Program...</h4></div>
        </center>
    </div>
    <div id="console-title-bar">
        <ul class="nav nav-tabs nav-justified">
            <li class="active tab-input"><a data-toggle="tab" href="https://www.onlinegdb.com/#tab-stdin">input</a></li>
            <li class="tab-stdout" style="display:none"><a data-toggle="tab" href="https://www.onlinegdb.com/#tab-stdout">stdout</a></li>
            <li class="tab-stderr" style="display:none"><a data-toggle="tab" href="https://www.onlinegdb.com/#tab-stderr">stderr</a></li>
            <li class="tab-debug" style="display:none"><a data-toggle="tab" href="https://www.onlinegdb.com/#tab-debug-console">Debug Console</a></li>
        </ul>
    </div>
    <div id="console-content" class="tab-content">
        <div id="tab-stdin" class="tab-pane fade in active">
            <div id="stdin-wrapper" style="z-index: 10; position: absolute; width: 100%; height: 100%; display: none;">
            <div style="height:37px; padding:5px 10px;  position:absolute;left:0px;right:0px;">
            <span style="float:left;width:20%;text-overflow: ellipsis;max-height:100%;overflow:hidden">Command line arguments:</span> <span style="display: block;"><input id="cmd_line_args" style="width:80%" name="cmd_line_args" value=""><br>
            </span></div>
            <div class="well" style="position:absolute; padding-top:0px; width:100%;top:37px; bottom:0px;border-radius:0px;padding:9px;">
                <div style="z-index:1">
                Standard Input: 
                <input type="radio" id="input_method_interactive" name="input_method" value="interactive" checked=""> Interactive Console
                    <input style="margin-left:50px;" type="radio" id="input_method_text" name="input_method" value="text"> Text<br>
                </div>
                    <div id="ad_unit_bottom_wrapper">
                        <div id="ad_unit_bottom">
                            
                            <!-- /8691100/OnlineGDB_S2S_Leaderboard_BTF -->
                            <div id="bsa-zone_1573224210072-0_123456" data-google-query-id="CPv98MmxvPsCFaHecwEdX3oOdA"><div id="google_ads_iframe_/8691100/OnlineGDB_S2S_Leaderboard_BTF_0__container__" style="border: 0pt none; margin: auto; text-align: center;"><iframe id="google_ads_iframe_/8691100/OnlineGDB_S2S_Leaderboard_BTF_0" name="google_ads_iframe_/8691100/OnlineGDB_S2S_Leaderboard_BTF_0" title="3rd party ad content" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" style="border: 0px; vertical-align: bottom;" data-load-complete="true" data-google-container-id="1" src="./fibonacci_files/saved_resource.html"></iframe></div></div>
                            <!--<div id="native-banner" class="native-standard"></div>-->
                            
                        </div>
                    </div>
                    <textarea class="form-control" id="stdinput" placeholder="Enter input to program here" style="height:100%; resize: none;  display:none "></textarea>
            </div>
            </div>
            <div id="interactive-terminal-container" style="position:absolute; margin:0px;top:0px; bottom:0px; left:0px; right:0px;" class="col-sm-121"><div dir="ltr" class="terminal xterm" tabindex="0" role="document"><div class="xterm-viewport" style="background-color: rgb(0, 0, 0);"><div class="xterm-scroll-area" style="height: 142px;"></div></div><div class="xterm-screen" style="width: 1129px; height: 142px;"><div class="xterm-helpers"><textarea class="xterm-helper-textarea" aria-label="Terminal input" aria-multiline="false" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="left: 252.292px; top: 68px; width: 9.01042px; height: 17px; line-height: 17px; z-index: -5;"></textarea><span class="xterm-char-measure-element" aria-hidden="true" style="font-family: courier-new, courier, monospace; font-size: 15px;">W</span><div class="composition-view"></div></div><canvas class="xterm-text-layer" width="1016" height="128" style="z-index: 0; width: 1129px; height: 142px;"></canvas><canvas class="xterm-selection-layer" width="1016" height="128" style="z-index: 1; width: 1129px; height: 142px;"></canvas><canvas class="xterm-link-layer" width="1016" height="128" style="z-index: 2; width: 1129px; height: 142px;"></canvas><canvas class="xterm-cursor-layer" width="1016" height="128" style="z-index: 3; width: 1129px; height: 142px;"></canvas></div></div></div>

        </div>
        <div id="tab-stdout" class="tab-pane fade">
            <div id="stdout-wrapper" class="well" style="border:none;height:100%;border-radius:0px;padding:9px; margin:0px;"><span id="ide-run-result"></span>
                <div id="stdout-container" style="position: absolute;    top: 30px;    bottom: 0px;    left: 10px;   right: 10px;">
                <pre class="msg" style="position: absolute;    top: 0px;    bottom: 0px;    left: 0px;    right: 0px;background-color: white;"></pre>
                </div>
            </div>
        </div>
        <div id="tab-stderr" class="tab-pane fade">
            <div id="stderr-wrapper" class="well" style="border:none;height:100%;border-radius:0px;padding:9px; margin:0px;"><span id="ide-compile-result"></span>
                <div id="stderr-container" style="position: absolute;    top: 30px;    bottom: 0px;    left: 10px;   right: 10px;">
                <pre class="msg" style="position: absolute;    top: 0px;    bottom: 0px;    left: 0px;    right: 0px;"></pre>
                </div>
            </div>
        </div>
        <div id="tab-debug-console" class="tab-pane fade">
            <div id="debug-console" style="border:none; height:100%; border-radius:0px;padding:0px; margin:0px;">
                <div class="inactive-content" style="color:#bdbdbd; padding-top:15px; text-align:center">
                    <h4>
                    Program is not being debugged. Click "Debug" button to start program in debug mode.
                        </h4>
                </div>
                <span id="debug-bar" style="display:none">
                    <button type="submit" id="debug_btn_run" class="btn btn-success" disabled="true" onclick="ide.debug(&#39;run&#39;)"><span class="glyphicon glyphicon-eject" aria-hidden="true" title="start"></span> start</button>
                    <button type="submit" id="debug_btn_pause" class="btn btn-warning" disabled="true" onclick="ide.debug(&#39;interrupt&#39;)"> <span class="glyphicon glyphicon-pause" aria-hidden="true" title="interrupt"></span> pause</button>
                    <button type="submit" id="debug_btn_cont" class="btn btn-primary" disabled="true" onclick="ide.debug(&#39;continue&#39;)"> <span class="glyphicon glyphicon-play" aria-hidden="true" title="continue"></span> continue</button>
                    <button type="submit" id="debug_btn_next" class="btn btn-primary" disabled="true" onclick="ide.debug(&#39;next&#39;)"> <span class="glyphicon glyphicon-step-forward" aria-hidden="true" title="next/step over"></span> step over</button>
                    <button type="submit" id="debug_btn_step" class="btn btn-primary" disabled="true" onclick="ide.debug(&#39;step&#39;)"> <span class="glyphicon glyphicon-forward" aria-hidden="true" title="step into"></span> step into</button>
                    <button type="submit" id="debug_btn_finish" class="btn btn-primary" disabled="true" onclick="ide.debug(&#39;finish&#39;)"> <span class="glyphicon glyphicon-fast-forward" aria-hidden="true" title="finish/step out"></span> step out</button>
                    
                    <a class="btn btn-success" href="https://www.onlinegdb.com/blog/brief-guide-on-how-to-use-onlinegdb-debugger/" target="_blank"> <span class="glyphicon glyphicon-info-sign" aria-hidden="true" title="Help : How to use debugger?"></span> help</a>
                    
                    </span>
                <div class="col-sm-121 active-content" style="position: absolute;    top: 24px;    bottom: 0px;    left: 0px;    right: 0px;">
                <div id="terminal-container" class="col-sm-12"></div>
                </div>

            </div>
        </div>
    </div>

</div>
                        <!-- middle bottom end -->
                    </div>
                </div>
            </div>
            <div class="split-pane-divider" id="my-divider2" style="left: 1171px;"><div class="split-pane-divider-inner"></div></div>
            <div class="split-pane-component" id="right-right-component" style="left: 1171px;">                
                <!-- right component start -->
                <div class="col-sm-41" id="debug-pan" style="background-color:#bdbdbd">
                    <div class="panel-group">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" class="collapse-toggle" href="https://www.onlinegdb.com/#debug_window_call_stack">Call Stack</a>
      </h4>
    </div>
    <div id="debug_window_call_stack" class="collapse in">
        <div class="table-responsive"><div class="JCLRgrips" style="width: 156.778px;"><div class="JCLRgrip" style="left: 19.5555px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip" style="left: 37.7673px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip JCLRLastGrip" style="left: 55.9791px; height: 26px;"></div></div><table class="table table-bordered JPadding JColResizer" id="JColResizer1">
       <thead> <tr><th style="width: 18.2222px;">#</th><th style="width: 18.2222px;">Function</th><th style="width: 18.2222px;">File:Line</th></tr></thead>
       <tbody></tbody>
       </table></div>
</div>
  </div>

  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" class="collapse-toggle" href="https://www.onlinegdb.com/#debug_window_local_variables">Local Variables</a>
      </h4>
    </div>
    <div id="debug_window_local_variables" class="collapse in">
        <div class="table-responsive"><div class="JCLRgrips" style="width: 111.778px;"><div class="JCLRgrip" style="left: 19.5555px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip JCLRLastGrip" style="left: 37.7673px; height: 26px;"></div></div><table class="table table-bordered JPadding JColResizer" id="JColResizer2">
       <thead> <tr><th style="width: 18.2222px;">Variable</th><th style="width: 18.2222px;">Value</th></tr></thead>
       <tbody></tbody>
       </table></div>
</div>
</div>

<div class="panel panel-default panel-registers">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" class="collapse-toggle" href="https://www.onlinegdb.com/#debug_window_registers">Registers</a>
      </h4>
    </div>
    <div id="debug_window_registers" class="collapse in">
        <div class="table-responsive"><table class="table table-bordered">
       <thead> <tr><th>Register</th><th>Value</th></tr></thead>
       <tbody></tbody>
       </table></div>
</div>
</div>

<div class="panel panel-default panel-display-expression">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" class="collapse-toggle" href="https://www.onlinegdb.com/#debug_window_display_expression">Display Expressions</a>
      </h4>
    </div>
    <div id="debug_window_display_expression" class="collapse in">
    <div class="table-responsive">
        <div class="JCLRgrips" style="width: 146.778px;"><div class="JCLRgrip" style="left: 19.5555px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip" style="left: 37.7673px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip JCLRLastGrip" style="left: 55.9791px; height: 26px;"></div></div><table class="table table-bordered JPadding JColResizer" style="margin-bottom:0px" id="JColResizer0">
       <thead><tr><th style="width: 18.2222px;">Expression</th><th style="width: 18.2222px;">Value</th><th style="width: 18.2222px;"></th></tr></thead>
       <tbody>
       </tbody>
       </table>
       <input id="input_watch_expr" class="col-sm-12" placeholder="Enter expression to watch">
    </div>
</div>
</div>

<div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" class="collapse-toggle" href="https://www.onlinegdb.com/#debug_window_breakpoints">Breakpoints and Watchpoints</a>
      </h4>
    </div>
    <div id="debug_window_breakpoints" class="collapse in">
        <div class="table-responsive"><div class="JCLRgrips" style="width: 139.778px;"><div class="JCLRgrip" style="left: 19.5555px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip" style="left: 37.7673px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip" style="left: 55.9791px; height: 26px;"><div class="JColResizer"></div></div><div class="JCLRgrip JCLRLastGrip" style="left: 74.1909px; height: 26px;"></div></div><table class="table table-bordered JPadding JColResizer" id="JColResizer3">
       <thead><tr><th style="width: 18.2222px;"></th><th style="width: 18.2222px;">#</th><th style="width: 18.2222px;">Description</th><th style="width: 18.2222px;"></th></tr></thead>
       <tbody></tbody>
       </table></div>
</div>
</div>

  </div>
</div> 
                <!-- right component end -->
            </div>
        </div>
        <div class="right-sidebar">
            <span id="right-sidebar-close" class="btn btn-info glyphicon glyphicon-menu-right"></span>
                

        </div>
    
    
    <script>
        $(document).ready(function() {
            Mousetrap.bind('f8', function() { trace_event('Key-F8'); $('#control-btn-debug').click(); return false;});
            Mousetrap.bind("f9", function() { trace_event('Key-F9'); $('#control-btn-run').click(); return false;});
            Mousetrap.bind(['command+s', 'ctrl+s'], function() { trace_event('Key-Ctrl+S'); $('#control-btn-save').click(); return false; });
            Mousetrap.bind(['command+b', 'ctrl+b'], function() { trace_event('Key-Ctrl+B'); $('#control-btn-beautify').click(); return false; });
            Mousetrap.bind(['command+m', 'ctrl+m'], function() { trace_event('Key-Ctrl+M'); $('#control-btn-newfile').click(); return false; });
        
            var editor = $("#multi_editor_container").editor();
            editor.setModeForLang($("#lang-select").val());

            

            
            
            

            editor.addEventListener('breakpoint_set', function (e) { 
                var bp = e.breakpoint;
                ide.setBreakpoint(bp);
            });
            editor.addEventListener('breakpoint_unset', function (e) { 
                var bp = e.breakpoint;
                ide.clearBreakpoint(bp);
            });
            $("#control-btn-newfile").on('click', function(){
                editor.new_editor();
                //track_event('control_menu', 'newfile');
            });

            $("#control-btn-upload").on('click', function(){
                ide.upload_file();
                //track_event('control_menu', 'upload');
            });
            $("#control-btn-save").on('click', function(){
                saveCode();
                //track_event('control_menu', 'save');
            });  

            ide.editor = editor;    
            //these guys can work after editor is initialized
            enable_btn('control-btn-',['save','share','beautify','download']);      
        });
        
        /*
        ace.require("ace/ext/language_tools");
        var editor = ace.edit("editor1");
        var editor2 = ace.edit("editor2");
        editor.getSession().setTabSize(4);
        editor.setFontSize('medium');
        editor.setTheme("ace/theme/idle_fingers");
        editor.getSession().setMode("ace/mode/c_cpp");
        // enable autocompletion and snippets
        editor.setOptions({
            enableBasicAutocompletion: true,
            enableSnippets: true,
            enableLiveAutocompletion: true
        });
        editor.on("guttermousedown", function(e){ 
           // if(!ide.gdbstarted) return;
            var Range = ace.require('ace/range').Range;

            var target = e.domEvent.target; 
            if (target.className.indexOf("ace_gutter-cell") == -1) 
                return; 

            if (e.clientX > 25 + target.getBoundingClientRect().left) 
                return; 

            var row = e.getDocumentPosition().row 

            if (target.className.indexOf("ace_breakpoint") == -1)
                ide.setBreakpoint(row+1, true);//e.editor.session.setBreakpoint(row)
            else
                ide.clearBreakpoint(row+1, true);//e.editor.session.clearBreakpoint(row)
            e.stop() 
        }); 
        
        editor.addBreakpoint = function(line, breaknumber) {
            if(!editor.breakpointList){
                editor.breakpointList = [];
            }
            editor.breakpointList[breaknumber] = line;
            console.log(editor.breakpointList);
        }
        */
        
        var project_uid = null;
        
        
    </script>
    
    <script>
        /*_native.init("CK7DC2JE", {
          targetClass: 'native-js'
        });*/
        </script>
<script>
    function track_event(arg1, arg2){
        //if(typeof ga !== 'undefined' && ga) ga('send', 'event', arg1, arg2);
        if(gtag)
        gtag('event', arg2, {
        'event_category': arg1
        });
    }
    function is_mobile(){
        return $('#mobile_test_element').css('display')=='none';
    }

    (function () {
        if(no_ads) return;
        if (typeof _bsa !== 'undefined' && _bsa) {
            /*_bsa.init('custom', 'CK7DC2JE', 'placement:onlinegdbcom', {
                target: '#native-inline',
                template: '<a href="##link##" target="_blank" rel="noopener" rel="nofollow"><div class="sponsor">Sponsor</div><div class="native-description">##company## — ##description##</div></a>'
            });*/
            
            if(!is_mobile()) {

            _bsa.init('custom', 'CK7I6K7M', 'placement:onlinegdbcom-top', {
                target: '#native-inline',
                template: `<a href="##link##" target="_blank" rel="noopener" rel="nofollow"><div class="sponsor">Sponsor</div><div class="native-description">##company## — ##description##</div></a>`
            });
            }
            if(!do_fallback_ad_check) {
            _bsa.init('custom', 'CK7DC2JE', 'placement:onlinegdbcom-banner', {
                target: '#native-banner',
                template: `
            <a href="##link##" class="native-banner" style="background: linear-gradient(-30deg, ##backgroundColor##E5, ##backgroundColor##E5 45%, ##backgroundColor## 45%) #fff;">
              <div class="native-main">
                <img class="native-img" img src="##logo##">
                <div class="native-details" style="color: ##textColor##">
                  <span class="native-company">Sponsored by ##company##</span>
                  <span class="native-desc">##description##</span>
                </div>
                <span class="native-cta" style="color: ##ctaTextColor##; background-color: ##ctaBackgroundColor##;">##callToAction##</span>
              </div>
            </a>
            <a class="native-via" href="##adViaLink##">Ads via BuySellAds</a>
            `
            });
            }
        } else {
            track_event('BSA Undefined', 'bsa_undefined');
        }
    })();
</script>

<script>
    /*
    _bsa.init('custom', 'CVADC53U', 'placement:onlinegdbcom', {
        target: '.native-js',
        template: '<a href="##link##" target="_blank" rel="noopener" rel="nofollow"><span class="sponsor">Sponsor</span> ##company## — ##description##</a>'
    });*/

    function fallback_native_top(){
        return false;
        
        var html = '<a href="/contribute" target="_blank" rel="noopener"><div class="sponsor">Contribute</div><div class="native-description">Submit a programming article and win assured Amazon gift voucher!!</div></a>';
        $("#native-inline").html(html);
        return true;
        
    }
    function process_no_bottom_adunit() {
        return;
        if(!do_fallback_ad_check) return;
        var script = document.createElement("script"); 
        script.src = "https://cdn.thisiswaldo.com/static/js/5831.js"; 
        script.type = "text/javascript"; 
        document.getElementById("ad_unit_bottom_wrapper").appendChild(script);
    }
    function BSANativeCallback(data) {
        if (data.segment=="placement:onlinegdbcom-top") {
            if((data.ads && data.ads.length > 0) || fallback_native_top())  {
                $("#editor-container").css('top', '37px');
                $("#editor_1").css('top', '57px');
                $("#title-bar").css('padding-top', '5px');
                $("#title-bar").css('padding-bottom', '5px');
                track_event('BSA Top AdUnit', 'bsa_top_adunit');
            } else {
                track_event('BSA No Top AdUnit', 'bsa_no_top_adunit');
            }
        } else if (data.segment=="placement:onlinegdbcom-banner") {
            if(data.ads && data.ads.length > 0) {
                track_event('BSA Bottom AdUnit', 'bsa_bottom_adunit');
            } else {
                process_no_bottom_adunit();
                track_event('BSA No Bottom AdUnit', 'bsa_no_bottom_adunit');
            }
        } else {
            track_event('BSA No AdUnit', 'bsa_no_adunit');
        }
    }
</script>

    

<!--<script src="//control.mockingfish.com/js/011503.js"></script>-->


    </div>
</div>
        </div>
    </div>
        </div>

    <!-- Runtime exceeds reason Modal -->
    <div id="runtimeModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Possible reasons for Runtime Exceed error</h4> </div>
                <div class="modal-body">
                    <p>
                    </p><ol>
                        <li>If your program is reading input from standard input and you forgot to provide input via stdin.</li>
                        <li>Your program contains infinite loop, which may never break.</li>
                        <li>Your program contains infinite recursive function calls.</li>
                        <li>May be your program is trying to process large data and it takes much time to process</li>
                    </ol>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- generic modal -->
    <div id="genericModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close modal-btn-close" data-dismiss="modal">×</button>
                    <h4 class="modal-title"></h4> </div>
                <div class="modal-body">
                </div>
                <div class="modal-footer">
                    <button type="button" class="ok-btn btn btn-default" data-dismiss="modal">Ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- New Version Available Modal -->
    <div id="newVersionModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">New Version Available</h4> </div>
                <div class="modal-body">
                    <p>
                    New Version of OnlineGDB is available. Please save your data and refresh page to update.
                </p></div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Console Output Modal -->
    <div id="consoleOutputModal" class="modal fade" role="dialog">
        <div class="modal-dialog" style="width:700px; height:90%">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Running Turbo C Project</h4> </div>
                <div class="modal-body">
                    <div class="dosbox-container">
                    <canvas id="jsdos">
                    </canvas>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Code Save Modal -->
    <div id="saveCodeModal" class="modal fade" role="dialog" style="display: none;">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Save Project</h4> </div>
                <div class="modal-body">
                    <div>
                        <form>
                        <div class="form-group">
                            <label for="name" class="name_label">Name of Project:</label>
                            <input type="text" class="form-control" id="project_name" value="">
                        </div>
                        <button type="button" class="btn btn-default btn_save">Save</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Compile Flags Modal -->
    <div id="compilerFlagsModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close hide" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Extra Compiler Flags</h4> </div>
                <div class="modal-body">
                    <div>
                        <form>
                        <div class="form-group">
                            <label for="name" class="name_label"></label>
                            <input type="text" class="form-control" id="compiler_flags" placeholder="You can set extra compiler flags here. Leave this empty if you don&#39;t know about it." value="">
                        </div>
                        <button type="button" class="btn btn-default btn_save" data-dismiss="modal">Ok</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Delete file Modal -->
    <div id="deleteFileModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <center><h4 class="modal-title">Are you sure you want to delete file `<span id="delete_file_name"></span>`?</h4> 
                    </center>
                    </div>
                <div class="modal-body">
                    <center>
                        <button type="button" class="btn btn-default btn-ok">Yes</button>
                        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>
                    </center>
                </div>
            </div>
        </div>
    </div>
    <!-- generic confirm Modal -->
    <div id="confirmModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <center><h4 class="modal-title"></h4></center>
                    </div>
                <div class="modal-body">
                    <center>
                        <button type="button" class="btn btn-default btn-ok">Yes</button>
                        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>
                    </center>
                </div>
            </div>
        </div>
    </div>
     <!-- New file Modal -->
    <div id="newFileModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">New File</h4> </div>
                <div class="modal-body">
                    <div>
                        <form>
                        <div class="form-group">
                            <label for="name">Name of new file:</label>
                            <input type="text" class="form-control" id="new_file_name" value="untitled">
                        </div>
                        <button type="button" class="btn btn-default btn-ok">ok</button>
                        <span class="error_message"></span>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Rename file Modal -->
    <div id="renameFileModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Rename File</h4> </div>
                <div class="modal-body">
                    <div>
                        <form>
                        <div class="form-group">
                            <label for="name">Name:</label>
                            <input type="text" class="form-control" id="edit_file_name" value="">
                        </div>
                        <button type="button" class="btn btn-default btn-ok">ok</button>
                        <button type="button" class="btn btn-default" data-dismiss="modal">cancel</button>
                        <span class="error_message"></span>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Code Share Modal -->
    <div id="shareCodeModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Share Link</h4> </div>
                <center class="msg">source code is copied to below link.</center>
                <div class="modal-body" style="text-align:center">
                    <p></p>
                </div>
            </div>
        </div>
    </div>
    <!-- Server disconnected Modal -->
    <div id="serverDisconnectedModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Lost connection to server</h4> </div>
                <div class="modal-body">
                    <p>Oops! Connection to server is lost. Please refresh the page to reconnect.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Debugging session stopped Modal -->
    <div id="myModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Debug session stopped</h4> </div>
                <div class="modal-body">
                    <p>Debug session is being stopped due to inactivity.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Debugging session stopped Modal -->
    <div id="noDebugPythonModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <center>
                    <h4 class="modal-title">Debug mode for <span class="lang">python</span> program is not yet supported.</h4> 
                    </center>
                    </div>
                    
                <div class="modal-footer">
                    <center>
                    <button type="button" class="btn btn-default" data-dismiss="modal">ok</button>
                    </center>
                </div>
            </div>
        </div>
    </div>
    <!-- login form modal -->
    <div id="loginModal" class="modal fade" role="dialog" style="display: none;">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Please login to save snippet to your personal account</h4> </div>
                <div class="modal-body">
                    <div style="width:100%">
                    <div class="omb_login">
                        <h3 class="omb_authTitle">Login with
                            <!--or <a href="#" style="font-size:24px; color:#337ab7">Sign up</a></h3>-->
                            <div class="row omb_row-sm-offset-31 omb_socialButtons">
                                <div class="col-xs-4">
                                    <a href="https://www.onlinegdb.com/#" onclick="login(&#39;googleplus&#39;)" class="btn btn-lg btn-block omb_btn-google">
                                        <i class="fa fa-facebook visible-xs"></i>
                                        <span class="hidden-xs">Google+</span>
                                    </a>
                                </div>
                                <div class="col-xs-4">
                                    <a href="https://www.onlinegdb.com/#" onclick="login(&#39;facebook&#39;)" class="btn btn-lg btn-block omb_btn-facebook">
                                        <i class="fa fa-twitter visible-xs"></i>
                                        <span class="hidden-xs">Facebook</span>
                                    </a>
                                </div>
                                <div class="col-xs-4">
                                    <a href="https://www.onlinegdb.com/#" onclick="login(&#39;github&#39;)" class="btn btn-lg btn-block omb_btn-github">
                                        <i class="fa fa-google-plus visible-xs"></i>
                                        <span class="hidden-xs">Github</span>
                                    </a>
                                </div>
                            </div>
                    </h3></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Run session stopped Modal -->
    <div id="myModalRun" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Run Console session stopped</h4> </div>
                <div class="modal-body">
                    <p>Run Console is being stopped due to inactivity.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">ok</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Add University Modal -->
    <div class="modal fade" id="myModalAddUniversity" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        <h4 class="modal-title" id="myModalLabel">Add School/Univeristy/Institute</h4>
      </div>
      <form method="post" action="https://www.onlinegdb.com/university">
      <div class="modal-body">
	   <div class="form-group">
		   <label for="university_name">School/University/Institute Name<span class="text-danger">*</span></label>
            <input type="text" class="form-control" name="university_name" id="university_name" placeholder="Enter university" required="">
          </div>
	  <div class="form-group">
		  <label for="state">State<span class="text-danger">*</span></label>
            <input type="text" class="form-control" name="state" id="state" placeholder="State" required="">
          </div>
	  <div class="form-group">
      	            <label for="country">Country<span class="text-danger">*</span></label>
		  <div class="btn-group bootstrap-select border rounded form-control h-50" style="width: 100%;"><button type="button" class="btn dropdown-toggle bs-placeholder btn-default" data-toggle="dropdown" role="button" title="Select Country"><span class="filter-option pull-left">Select Country</span>&nbsp;<span class="bs-caret"><span class="caret"></span></span></button><div class="dropdown-menu open" role="combobox"><div class="bs-searchbox"><input type="text" class="form-control" autocomplete="off" role="textbox" aria-label="Search"></div><ul class="dropdown-menu inner" role="listbox" aria-expanded="false"><li class="hidden is-hidden selected" data-original-index="0"><a tabindex="0" class="" data-tokens="null" role="option" aria-disabled="false" aria-selected="true"><span class="text">Select Country</span><span class="glyphicon glyphicon-ok check-mark"></span></a></li></ul></div><select class="selectpicker border rounded form-control h-50" name="country" data-width="100%" data-show-subtext="true" data-live-search="true" required="" tabindex="-98">
			  <option data-hidden="true" value="">Select Country</option>
			
                        </select></div>
	</div>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-success" onclick="addNewUniversity()">Submit</button>
      </div>
      </form>
    </div>
  </div>
</div>
    <!-- Editor Info Modal -->
    <div id="infoModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h4 class="modal-title">Keyboard Shortcuts</h4> </div>
                <div class="modal-body"> <pre><b>IDE Shortcuts:</b>
New file : Ctrl-M
Run Code : F9
Debug Code : F8
Save Project : Ctrl-S
Beautify Code : Ctrl-B
Settings Menu : Ctrl-Shift-S
Info : Ctrl-I

<b>Editor Shortcuts:</b>
showSettingsMenu : Ctrl-,
goToNextError : Alt-E
goToPreviousError : Alt-Shift-E
selectall : Ctrl-A
gotoline : Ctrl-L
fold : Alt-L|Ctrl-F1
unfold : Alt-Shift-L|Ctrl-Shift-F1
toggleFoldWidget : F2
toggleParentFoldWidget : Alt-F2
foldOther : Alt-0
unfoldall : Alt-Shift-0
findnext : Ctrl-K
findprevious : Ctrl-Shift-K
selectOrFindNext : Alt-K
selectOrFindPrevious : Alt-Shift-K
find : Ctrl-F
overwrite : Insert
selecttostart : Ctrl-Shift-Home
gotostart : Ctrl-Home
selectup : Shift-Up
golineup : Up
selecttoend : Ctrl-Shift-End
gotoend : Ctrl-End
selectdown : Shift-Down
golinedown : Down
selectwordleft : Ctrl-Shift-Left
gotowordleft : Ctrl-Left
selecttolinestart : Alt-Shift-Left
gotolinestart : Alt-Left|Home
selectleft : Shift-Left
gotoleft : Left
selectwordright : Ctrl-Shift-Right
gotowordright : Ctrl-Right
selecttolineend : Alt-Shift-Right
gotolineend : Alt-Right|End
selectright : Shift-Right
gotoright : Right
selectpagedown : Shift-Pagedown
gotopagedown : Pagedown
selectpageup : Shift-Pageup
gotopageup : Pageup
scrollup : Ctrl-Up
scrolldown : Ctrl-Down
selectlinestart : Shift-Home
selectlineend : Shift-End
togglerecording : Ctrl-Alt-E
replaymacro : Ctrl-Shift-E
jumptomatching : Ctrl-P
selecttomatching : Ctrl-Shift-P
expandToMatching : Ctrl-Shift-M
removeline : Ctrl-D
duplicateSelection : Ctrl-Shift-D
sortlines : Ctrl-Alt-S
togglecomment : Ctrl-/
toggleBlockComment : Ctrl-Shift-/
modifyNumberUp : Ctrl-Shift-Up
modifyNumberDown : Ctrl-Shift-Down
replace : Ctrl-H
undo : Ctrl-Z
redo : Ctrl-Shift-Z|Ctrl-Y
copylinesup : Alt-Shift-Up
movelinesup : Alt-Up
copylinesdown : Alt-Shift-Down
movelinesdown : Alt-Down
del : Delete
backspace : Shift-Backspace|Backspace
cut_or_delete : Shift-Delete
removetolinestart : Alt-Backspace
removetolineend : Alt-Delete
removewordleft : Ctrl-Backspace
removewordright : Ctrl-Delete
outdent : Shift-Tab
indent : Tab
blockoutdent : Ctrl-[
blockindent : Ctrl-]
transposeletters : Ctrl-T
touppercase : Ctrl-U
tolowercase : Ctrl-Shift-U
expandtoline : Ctrl-Shift-L
addCursorAbove : Ctrl-Alt-Up
addCursorBelow : Ctrl-Alt-Down
addCursorAboveSkipCurrent : Ctrl-Alt-Shift-Up
addCursorBelowSkipCurrent : Ctrl-Alt-Shift-Down
selectMoreBefore : Ctrl-Alt-Left
selectMoreAfter : Ctrl-Alt-Right
selectNextBefore : Ctrl-Alt-Shift-Left
selectNextAfter : Ctrl-Alt-Shift-Right
splitIntoLines : Ctrl-Alt-L
alignCursors : Ctrl-Alt-A
findAll : Ctrl-Alt-K
showKeyboardShortcuts : Ctrl-Alt-H
          </pre> </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
    <script>
    var isLoggedIn =  false;
    var isTinyide =  false; 
    var isStudentSubmission =  false ;

    function track_event(arg1, arg2, arg3){
        //if(ga) ga('send', 'event', arg1, arg2, arg3);
        if(gtag)
        gtag('event', arg2, {
        'event_category': arg1,
        'event_label': arg3
        });
    }
    var check_fallback_ad_timer = null;
    function repalce_fallback_ad(){
    
    }
    function check_fallback_ad_helper(){
        var ad_text = $("#ad_wrapper").text();
        //track_event('Check Fallback Ad', 'check_fallback_ad');

        if(ad_text.indexOf("ads via")>-1){// ad is loaded
            if(ad_text.indexOf("Have fun taking surveys and get paid!")>-1){// fallback ad 
                repalce_fallback_ad();
            }
            clearInterval(check_fallback_ad_timer);
        }
    }
    function check_fallback_ad(){
        check_fallback_ad_timer = setInterval(check_fallback_ad_helper, 2000); // check every 2 seconds
    }
    function update_snippet_datetime(){
        
    }
    $(document).ready(function() {
        $('div.split-pane').splitPane();
        if(do_fallback_ad_check)
            check_fallback_ad();
        update_snippet_datetime();

            $( ".ogdb-local-date" ).each(function( index ) {
        var ogdb_date = $(this).attr('ogdb-local-date');
        if(ogdb_date!='')
            ogdb_date = new Date(ogdb_date).toLocaleString([], { hour12: true});
        else
            ogdb_date = "Invalid Date";
        $(this).text(ogdb_date);
        });
    });
    </script>
    
    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="./fibonacci_files/js(1)"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  
  gtag('config', 'UA-79897653-2');
  
</script>




<!--
<script>
window['_fs_debug'] = false;
window['_fs_host'] = 'fullstory.com';
window['_fs_org'] = 'B881V';
window['_fs_namespace'] = 'FS';
(function(m,n,e,t,l,o,g,y){
    if (e in m) {if(m.console && m.console.log) { m.console.log('FullStory namespace conflict. Please set window["_fs_namespace"].');} return;}
    g=m[e]=function(a,b){g.q?g.q.push([a,b]):g._api(a,b);};g.q=[];
    o=n.createElement(t);o.async=1;o.src='https://'+_fs_host+'/s/fs.js';
    y=n.getElementsByTagName(t)[0];y.parentNode.insertBefore(o,y);
    g.identify=function(i,v){g(l,{uid:i});if(v)g(l,v)};g.setUserVars=function(v){g(l,v)};
    y="rec";g.shutdown=function(i,v){g(y,!1)};g.restart=function(i,v){g(y,!0)};
    g.identifyAccount=function(i,v){o='account';v=v||{};v.acctId=i;g(o,v)};
    g.clearUserCookie=function(){};
})(window,document,window['_fs_namespace'],'script','user');
</script>
-->
        <!-- Go to www.addthis.com/dashboard to customize your tools --> <script type="text/javascript" src="./fibonacci_files/addthis_widget.js.download"></script><div id="_atssh" style="visibility: hidden; height: 1px; width: 1px; position: absolute; top: -9999px; z-index: 100000;"><iframe id="_atssh380" title="AddThis utility frame" style="height: 1px; width: 1px; position: absolute; top: 0px; z-index: 100000; border: 0px; left: 0px;" src="./fibonacci_files/sh.f48a1a04fe8dbf021b4cda1d.html"></iframe></div><style id="service-icons-0"></style> 
<!--<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-57a770c71976bf87"></script>-->
<!--Start of Tawk.to Script-->

<!--End of Tawk.to Script-->



<!--   <script src="https://cdn.ravenjs.com/3.14.2/raven.min.js" crossorigin="anonymous"></script>
    <script>Raven.config('https://33e437c2b49247e2995f75c8bde618e1@sentry.io/164141').install();</script>-->

<script>(function(){var js = "window['__CF$cv$params']={r:'76cff714383e9aa1',m:'rfX.WGyXDHPPHxACv5vk5xXRGTaecsfJdWN4qeJGupE-1668934511-0-AX72+vBi0JSF6f0+f9mlO+iCONw5VP5eQptj1aZu5yvTF46GQq6vkrvvonG3D/3YzgpDf4Tu77pQ9D9RmTc9GQ8pRDskV0bnxKl/gwRWM8Isdyz/r2NRciPzJuSoPZ5ETA==',s:[0x9c38b7a62c,0x594e03a936],u:'/cdn-cgi/challenge-platform/h/b'};var now=Date.now()/1000,offset=14400,ts=''+(Math.floor(now)-Math.floor(now%offset)),_cpo=document.createElement('script');_cpo.nonce='',_cpo.src='/cdn-cgi/challenge-platform/h/b/scripts/alpha/invisible.js?ts='+ts,document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = '';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[0].appendChild(_0xj);}}if (document.readyState !== 'loading') {handler();} else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);} else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();}};}})();</script><iframe src="./fibonacci_files/container.html" style="visibility: hidden; display: none;"></iframe><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;" src="./fibonacci_files/saved_resource(4).html"></iframe>


<iframe id="adg-0-sync" height="0" width="0" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="./fibonacci_files/user_sync.html" style="border: 0px; display: none;"></iframe><iframe id="adg-1-sync" height="0" width="0" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="./fibonacci_files/multi-sync.html" style="border: 0px; display: none;"></iframe><iframe name="google_ads_top_frame" id="google_ads_top_frame" style="display: none; position: fixed; left: -999px; top: -999px; width: 0px; height: 0px;" src="./fibonacci_files/saved_resource(5).html"></iframe><img id="adg-2-sync" style="position:absolute; display:none; height:0; width:0;" src="./fibonacci_files/occ"><iframe src="./fibonacci_files/syncframe.html" width="0" height="0" frameborder="0" title="Criteo GUM iframe" style="border-width: 0px; margin: 0px; display: none;"></iframe><iframe src="./fibonacci_files/aframe.html" width="0" height="0" style="display: none;"></iframe></body><iframe sandbox="allow-scripts allow-same-origin" id="38cb9b1d20b993b" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/beacon.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="39df0e26e7be9bc" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/user_sync(1).html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="40f3191fcf185ce" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/saved_resource(6).html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="416979288adc0f2" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/ixmatch.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="4221cc6d77582e3" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/usync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="43e674975d83ede" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/sync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="4441b8190c01018" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/checksync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="450c6d41574339e" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/pd.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="4644f1661248314" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/async_usersync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="47ca4fed05a7dc3" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./fibonacci_files/iframe.html">
    </iframe></html>