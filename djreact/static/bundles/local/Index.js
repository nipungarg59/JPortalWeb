webpackJsonp([1],{0:function(e,t,n){try{(function(){"use strict";"use-strict";function e(e){return e&&e.__esModule?e:{default:e}}function t(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function l(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function r(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}var o=function(){function e(e,t){for(var n=0;n<t.length;n++){var l=t[n];l.enumerable=l.enumerable||!1,l.configurable=!0,"value"in l&&(l.writable=!0),Object.defineProperty(e,l.key,l)}}return function(t,n,l){return n&&e(t.prototype,n),l&&e(t,l),t}}(),a=n(51),u=e(a),i=n(98),c=n(99),f=e(c),s=function(e){function n(){return t(this,n),l(this,(n.__proto__||Object.getPrototypeOf(n)).apply(this,arguments))}return r(n,e),o(n,[{key:"render",value:function(){return u.default.createElement("div",{className:"container-fluid login"},u.default.createElement(f.default,null))}}]),n}(u.default.Component);(0,i.render)(u.default.createElement(s,null),document.getElementById("Index"))}).call(this)}finally{}},98:function(e,t,n){"use strict";e.exports=n(64)},99:function(e,t,n){try{(function(){"use strict";"use-strict";function e(e){return e&&e.__esModule?e:{default:e}}function l(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function r(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function o(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=function(){function e(e,t){for(var n=0;n<t.length;n++){var l=t[n];l.enumerable=l.enumerable||!1,l.configurable=!0,"value"in l&&(l.writable=!0),Object.defineProperty(e,l.key,l)}}return function(t,n,l){return n&&e(t.prototype,n),l&&e(t,l),t}}(),u=n(51),i=e(u),c=function(e){function t(e){l(this,t);var n=r(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,e));return n.state={logdedIn:!1},n}return o(t,e),a(t,[{key:"render",value:function(){return this.state.logdedIn?i.default.createElement("div",null,i.default.createElement("h2",null,"Successfully Logged in")):i.default.createElement("div",{className:"container login-modal"},i.default.createElement("div",{className:"login-text-color login-heading1"},"JIIT Portal"),i.default.createElement("div",{className:"login-text-color"},i.default.createElement("span",{className:"login-heading2"},"Welcome Back"),i.default.createElement("br",null),i.default.createElement("span",{className:"login-heading3"},"Sign into your account.")),i.default.createElement("form",null,i.default.createElement("div",{className:"form-group login-input-field"},i.default.createElement("input",{type:"text",className:"form-control login-input-field-placeholder",placeholder:"Enrollment Number"})),i.default.createElement("div",{className:"form-group login-input-field"},i.default.createElement("input",{type:"text",className:"form-control login-input-field-placeholder",placeholder:"DOB(dd-mm-yyyy)"})),i.default.createElement("div",{className:"form-group login-input-field"},i.default.createElement("input",{type:"password",className:"form-control login-input-field-placeholder",placeholder:"Password"}))),i.default.createElement("button",{className:"btn btn-primary submit-button"},i.default.createElement("span",null,"Submit")),i.default.createElement("div",{className:"login-text-color login-heading3"},i.default.createElement("a",null,"Forget Password?")))}}]),t}(i.default.Component);t.default=c}).call(this)}finally{}}});