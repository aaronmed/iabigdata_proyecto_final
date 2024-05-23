<template>
  <v-container>
    <v-row class="my-12" v-if="showButtons">
      <v-col cols="12" md="12">
        <v-img
          class="mx-auto"
          max-height="300"
          max-width="1300"
          src="../assets/vaccine.jpg"
        ></v-img>
      </v-col>
      <v-col cols="12" md="12" class="d-flex justify-center">
        <div class="text-center text-h1 my-10">
          ¿Qué vacuna quieres predecir?
        </div>
      </v-col>
      <v-col cols="12" md="6">
        <v-btn
          class="pa-16 white--text text-h4"
          block
          x-large
          color="blue darken-2"
          @click="showComponent('h1n1')"
          >VACUNA PARA EL H1N1</v-btn
        >
      </v-col>
      <v-col cols="12" md="6">
        <v-btn
          class="pa-16 white--text text-h4"
          block
          x-large
          color="indigo darken-2"
          @click="showComponent('seasonal')"
          >VACUNA GRIPE ESTACIONAL</v-btn
        >
      </v-col>
    </v-row>
    <div v-if="!showButtons">
      <component :is="currentComponent"></component>
    </div>
  </v-container>
</template>

<script>
import H1N1Vaccine from "./H1N1Vaccine.vue";
import SeasonalVaccine from "./SeasonalVaccine.vue";

export default {
  name: "SelectorVaccine",
  data() {
    return {
      showButtons: true,
      currentComponent: null,
    };
  },
  methods: {
    showComponent(type) {
      this.showButtons = false;
      if (type === "h1n1") {
        this.currentComponent = "H1N1Vaccine";
      } else if (type === "seasonal") {
        this.currentComponent = "SeasonalVaccine";
      }
    },
  },
  components: {
    H1N1Vaccine,
    SeasonalVaccine,
  },
};
</script>
<style>
.white--text {
  color: white !important;
}
</style>
