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
          url: '/'
        },
        {
          text: 'What Can You Do?',
          items: 
          [
            { text: 'Become Aware' ,
              items: 
              [
                { text: 'Why Your Vote Matters' },
                { text: 'How to Become a Registered Voter' },
                { text: 'Register to Vote' }
              ]
            },
            { text: 'Be Informed' ,
              items: 
              [
                { text: 'Making Power Accessible' },
                { text: 'Tools and Resources' },
                { text: 'Making Your Plan to Vote' },
                { text: 'Go Vote' },
                { text: 'Guides',
                  items:
                  [
                    {text: 'Canvassing'}
                  ] 
                }
              ]
            },
            { text: 'Get Active' ,
              items: 
              [
                { text: 'Build Your Community/Expand Your Power' ,
                  items:
                  [
                    { text: 'How?',
                      items:
                      [
                        { text: 'Tell your friends' },
                        { text: 'Volunteer' ,
                          url: '/volunteer'}

                      ]
                    }
                  ] 
                },
                { text: 'Student Rep Program' },
                { text: 'Current Initiatives',
                  items:
                  [
                    { text: 'Water for all ordinance' },
                    { text: 'UN CEDAW' },
                    { text: 'Legislation' }
                  ]
                },
                { text: 'Go Vote' },
                { text: 'Guides',
                  items:
                  [
                    {text: 'Canvassing'}
                  ] 
                },
              ]
            }
          ]
        },
        {
          text: 'About Us',
          items: 
          [
            { text: 'Mission History' },
            { text: 'Our Team' ,
              url: '/whoweare'
            },
            { text: 'Our Impact',
              items:
              [
                { text: 'Work we\'ve done to date' },
                { text: 'Legislation passed' }
              ] 
            },
            { text: 'News' ,
              items:
              [
                { text: 'Articles & Features' ,
                  url: '/blog'
                },
                { text: 'SVI Newsletters' }
              ]
            },
            { text: 'Testimonials'},
            { text: 'Photos'},
            { text: 'Videos'}
          ]
        },
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
