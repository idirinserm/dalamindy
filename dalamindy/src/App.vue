<template>
  <div id="app">
    <img alt="Vue logo" :src="require('@/assets/LogoDalamindy.png')">
    <h1>Votre plateforme de cours en ligne</h1>

    <!-- Button at the top-right -->
    <div class="top-right-button">
      <v-menu open-on-hover>
        <template v-slot:activator="{ props }">
          <v-btn color="primary" v-bind="props">Dropdown</v-btn>
        </template>

        <v-list>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data: () => ({
    items: [
      { title: 'Cours' },
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
  justify-content: center;
  height: 100vh;
}

.top-right-button {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
