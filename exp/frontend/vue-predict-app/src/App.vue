<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./assets/syringe.png"
          transition="scale-transition"
          width="40"
        />
        Predicción de vacunación para la gripe H1N1 y gripe estacional
      </div>
    </v-app-bar>

    <v-main>
      <SelectorVaccine/>
    </v-main>
  </v-app>
</template>

<script>
import SelectorVaccine from './components/SelectorVaccine.vue';

export default {
  name: 'App',
  mounted() {
    document.title = "Predicción de las vacunas para la gripe estacional y H1N1";
  },

  components: {
    SelectorVaccine,
  },

  data: () => ({
    //
  }),
};
</script>
