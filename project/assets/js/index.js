'use strict';

import Vue from 'vue';
import Hello from './vue/hello.vue';

document.addEventListener('DOMContentLoaded', function() {
    Vue.component('hello', Hello)

    const app = new Vue({
        el: '#app'
    });
});
