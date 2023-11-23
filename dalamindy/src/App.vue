<template>
  <div id="app">
    <header>
      <h1>Votre plateforme de cours en ligne</h1>
      <img alt="Vue logo" :src="require('@/assets/LogoDalamindy.png')" class="logo">

      <div class="top-right-button">
        <v-menu open-on-hover>
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props">Dropdown</v-btn>
          </template>

          <v-list>
            <v-list-item v-for="(item, index) in items" :key="index">
              <v-btn v-if="item.title === 'Programme'" @click="redirectToProgrammePage">{{ item.title }}</v-btn>
              <v-list-item-title v-else>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    redirectToProgrammePage() {
      this.$router.push({ name: 'Programme' });
    },
  },
  data: () => ({
    items: [
      { title: 'Programme' },
      { title: 'Profil' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
  }),
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100vh;
  padding-top: 30px;
}

.logo {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 10%;
}

.top-right-button {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
