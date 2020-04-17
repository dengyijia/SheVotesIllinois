<template>
  <div class="blog">
    <br>
    <img alt="Vue logo" src="../assets/logo.png">
    <h1 class="center">She Blogs</h1>
    <h2 class="center">A Blog for She Votes Illinois</h2>
    <div class="body">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.body{
  text-align: left;
  margin: 5em 20em;
}
.center {
  text-align: center;
}
.headline {
  text-transform: uppercase;
  margin: 4rem auto;
  font-size: 4rem;
}
img {
  display: block;
  margin: 0 auto;
  width: 150px;
}
h2 {
  color: #35495e;
  text-transform: capitalize;
  margin-bottom: 2rem;
}
h3 {
  color: #2fd0d0;
  margin-bottom: 0;
  cursor: pointer;
  &:hover {
    text-decoration: underline;
  }
  .subtitle {
    color: grey;
    font-size: .98rem;
    float: right;
    font-weight: normal;
  }
}
p {
  margin-top: .4rem;
}
.sections {
  max-width: 40vw;
  margin: 0 auto;
  margin-top: 4rem;
}
.section {
  margin-bottom: 3rem;
}
.group {
  margin-bottom: 4rem;
}
</style>
