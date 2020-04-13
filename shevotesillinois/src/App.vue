<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 0px
}

 @import url('https://fonts.googleapis.com/css?family=Roboto');
  html { font-size: 22px; }
  body { font-family: 'Roboto', sans-serif; }
  a {
    color: #0094FF;
    text-decoration: none;
  }
  a:hover { color: #0074C6; }
</style>
