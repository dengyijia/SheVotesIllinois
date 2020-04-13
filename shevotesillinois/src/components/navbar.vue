<template>
<div>
<ejs-menu :items='menuItems'></ejs-menu>
</div>
</template>

<script>
import Vue from 'vue';
import { MenuPlugin } from '@syncfusion/ej2-vue-navigations';
import { enableRipple } from '@syncfusion/ej2-base';

enableRipple(true);
Vue.use(MenuPlugin);

export default {
   data: function() {
    return {
    //Menu items definition
      menuItems:  
      [
        {
          text: 'Home',
        },
        {
          text: 'Get Active',
        },
        {
          text: 'Become Aware',
          items: 
          [
            { text: 'Submenu' ,
              items: 
              [
                { text: 'Become Aware 1' },
                { text: 'Become Aware 2' }
              ]
            },
            { text: 'Sidebar' }
          ]
        },
        {
          text: 'Be Informed',
          items: 
          [
            { text: 'Spelling & Grammar' },
            { text: 'Customize' },
            { text: 'Options' }
          ]
        },
        { text: 'Go' },
        { text: 'Help' }
      ]
    };
  }
}
</script>

<style>
@import "../../node_modules/@syncfusion/ej2-base/styles/material.css";
@import "../../node_modules/@syncfusion/ej2-popups/styles/material.css";
@import "../../node_modules/@syncfusion/ej2-navigations/styles/material.css";

body {
  margin-top: 100px;
  text-align: center;
}
</style>
