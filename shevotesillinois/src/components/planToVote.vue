<template>
  <div class="home">
    <navbar></navbar>
    <br>
    <img alt="Vue logo" src="../assets/logo.png">
    <h1 class="center"></h1>
    <div class="sections">
      <div v-for="(section, index) in Object.keys(entries)" :key="index" class="group">
        <component v-bind:is="entries[section][0].sectionis">
          <template v-slot:header>{{section}}</template>

          <template class="lg" v-slot:lead>
            {{entries[section][0].sectiontext}}
          </template>
          <ul v-for="entry in entries[section]" :key="entry.id">
            <div v-if="entry.id === 'bullet'">
              <div class="entry">
                <li>
                    <a :href=entry.link>{{entry.text}}</a>
                    <ul class="lg" v-for="sub in entry.sublist" :key="sub.id">
                        <li><a :href=sub.link>{{sub.linktext}}</a>{{sub.text}}</li>
                    </ul>
                </li>
              </div>
            </div>
          </ul>
        </component>
      </div>
    </div>
  </div>
</template>

<script>
import COMPONENTS from '@/assets/plantovote.json';

export default {
  name: 'home',
  computed: {
    entries() {
      return COMPONENTS;
    },
  },
};
</script>
<style lang="scss" scoped>
a {
  color: #2fd0d0;
}
div {
  padding-right: 5px;
}
button{
  padding-right: 10px
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
  max-width: 80vw;
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
