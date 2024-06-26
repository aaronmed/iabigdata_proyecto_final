<template>
  <div class="mx-5 my-5">
    <v-img
      class="mx-auto"
      max-height="250"
      max-width="1200"
      src="../assets/seasonal.jpg"
    ></v-img>
    <v-card class="pa-10 ma-10" v-if="!submitted" color="blue-grey lighten-5">
      <v-card-title
        >Predicción de la vacuna de la gripe estacional</v-card-title
      >
      <v-form @submit.prevent="submitForm">
        <v-row>
          <!-- Column for Selects -->
          <v-col cols="12" md="6">
            <v-select
              v-model="form.h1n1_concern"
              :items="concernLevels"
              label="Nivel de preocupación por la gripe H1N1"
              required
            ></v-select>
            <v-select
              v-model="form.opinion_h1n1_vacc_effective"
              :items="effectivenessLevels"
              label="¿Qué opina sobre la efectividad de la vacuna contra la H1N1?"
              required
            ></v-select>
            <v-select
              v-model="form.opinion_h1n1_risk"
              :items="riskLevels"
              label="¿Qué opina sobre el riesgo de enfermarse de gripe H1N1 sin la vacuna?"
              required
            ></v-select>
            <v-select
              v-model="form.opinion_seas_vacc_effective"
              :items="effectivenessLevels"
              label="¿Qué opina sobre la efectividad de la vacuna contra la gripe estacional?"
              required
            ></v-select>
            <v-select
              v-model="form.opinion_seas_risk"
              :items="riskLevels"
              label="¿Qué opina sobre el riesgo de enfermarse de gripe estacional sin la vacuna?"
              required
            ></v-select>
          </v-col>

          <!-- Column for Radio Buttons -->
          <v-col cols="12" md="6">
            <v-select
              v-model="form.doctor_recc_h1n1"
              :items="yesNoOptions"
              label="¿Le recomendó el doctor la vacuna para la gripe H1N1?"
              required
            ></v-select>
            <v-select
              v-model="form.doctor_recc_seasonal"
              :items="yesNoOptions"
              label="¿Le recomendó el doctor la vacuna para la gripe estacional?"
              required
            ></v-select>
            <v-select
              v-model="form.chronic_med_condition"
              :items="yesNoOptions"
              label="¿Tiene alguna de las siguientes condiciones médicas crónicas: asma u otra afección pulmonar, diabetes, una afección cardíaca, una afección renal, anemia falciforme u otra anemia, una afección neurológica o neuromuscular, una afección hepática o un sistema inmunitario debilitado causado por una enfermedad crónica o por medicamentos tomados para una enfermedad crónica?"
              required
            ></v-select>
            <v-select
              v-model="form.health_worker"
              :items="yesNoOptions"
              label="¿Trabaja en el sector de sanidad?"
              required
            ></v-select>
            <v-select
              v-model="form.age_group"
              :items="ageOptions"
              label="¿Qué edad tiene?"
              required
            ></v-select>
          </v-col>
        </v-row>
        <v-btn block type="submit" @click="predictSeasonal()" color="primary">
          Predecir<v-icon> mdi-charity-search </v-icon></v-btn
        >
      </v-form>
    </v-card>

    <v-expansion-panels v-if="submitted" class="px-10 py-5">
      <v-expansion-panel>
        <v-expansion-panel-header color="blue-grey lighten-5" class="text-h4"
          >DATOS ENVIADOS</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          <v-alert color="blue lighten-4" class="mt-4">
            <p>
              <strong>Nivel de preocupación por la gripe H1N1:</strong>
              {{ form.h1n1_concern }}
            </p>
            <p>
              <strong>Rango de edad:</strong>
              {{ form.age_group }}
            </p>
            <p>
              <strong>Recomendación del doctor para la vacuna H1N1:</strong>
              {{ form.doctor_recc_h1n1 }}
            </p>
            <p>
              <strong
                >Recomendación del doctor para la vacuna estacional:</strong
              >
              {{ form.doctor_recc_seasonal }}
            </p>
            <p>
              <strong>Condiciones médicas crónicas:</strong>
              {{ form.chronic_med_condition }}
            </p>
            <p>
              <strong>Trabaja en el sector de sanidad:</strong>
              {{ form.health_worker }}
            </p>
            <p>
              <strong
                >Opinión sobre la efectividad de la vacuna contra H1N1:</strong
              >
              {{ form.opinion_h1n1_vacc_effective }}
            </p>
            <p>
              <strong>Riesgo de enfermarse de gripe H1N1 sin la vacuna:</strong>
              {{ form.opinion_h1n1_risk }}
            </p>
            <p>
              <strong
                >Opinión sobre la efectividad de la vacuna contra la gripe
                estacional:</strong
              >
              {{ form.opinion_seas_vacc_effective }}
            </p>
            <p>
              <strong
                >Riesgo de enfermarse de gripe estacional sin la vacuna:</strong
              >
              {{ form.opinion_seas_risk }}
            </p>
          </v-alert>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-layout
      v-if="loading"
      class="my-10"
      align-center
      justify-center
      column
      fill-height
    >
      <v-flex row align-center>
        <v-progress-circular
          indeterminate
          :size="50"
          color="primary"
          class=""
        ></v-progress-circular>
      </v-flex>
    </v-layout>

    <v-alert
      class="pa-15 my-5 text-h1 text-center"
      v-if="prediction == 1"
      color="green lighten-2"
      >VACUNADO</v-alert
    >
    <v-alert
      class="pa-15 my-5 text-h1 text-center"
      v-if="prediction == 0"
      color="red lighten-3"
      >NO VACUNADO</v-alert
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SeasonalVaccine",
  data() {
    return {
      form: {
        h1n1_concern: "",
        doctor_recc_h1n1: "",
        doctor_recc_seasonal: "",
        chronic_med_condition: "",
        health_worker: "",
        opinion_h1n1_vacc_effective: "",
        opinion_h1n1_risk: "",
        opinion_seas_vacc_effective: "",
        opinion_seas_risk: "",
        age_group: "",
      },
      concernLevels: [
        { text: "Nada preocupado", value: 0 },
        { text: "Poco preocupado", value: 1 },
        { text: "Algo preocupado", value: 2 },
        { text: "Muy preocupado", value: 3 },
      ],
      knowledgeLevels: [
        { text: "Sin conocimiento", value: 0 },
        { text: "Poco conocimiento", value: 1 },
        { text: "Mucho conocimiento", value: 2 },
      ],
      effectivenessLevels: [
        { text: "Nada efectiva", value: 1 },
        { text: "Poco efectiva", value: 2 },
        { text: "No sabe", value: 3 },
        { text: "Algo efectiva", value: 4 },
        { text: "Muy efectiva", value: 5 },
      ],
      riskLevels: [
        { text: "Muy bajo", value: 1 },
        { text: "Algo bajo", value: 2 },
        { text: "No sabe", value: 3 },
        { text: "Algo alto", value: 4 },
        { text: "Muy alto", value: 5 },
      ],
      yesNoOptions: [
        { text: "Sí", value: 1 },
        { text: "No", value: 0 },
      ],
      ageOptions: [
        { text: "18 - 34 años", value: 0 },
        { text: "35 - 44 años", value: 1 },
        { text: "45 - 54 años", value: 2 },
        { text: "55 - 64 años", value: 3 },
        { text: "65+ años", value: 4 },
      ],
      submitted: false,
      prediction: -1,
      loading: false,
    };
  },
  methods: {
    submitForm() {
      this.submitted = true;
      console.log(this.form);
    },

    async predictSeasonal() {
      this.loading = true;
      let endpoint = "http://localhost:5000/predict_seasonal";
      try {
        const response = await axios.post(endpoint, {
          input_data: this.form,
        });
        this.prediction = response.data.prediction;
        this.loading = false;
      } catch (error) {
        console.error("Error during prediction:", error);
      }
    },
  },
};
</script>
