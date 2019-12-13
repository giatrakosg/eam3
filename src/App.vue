<template>
  <v-app>
    <v-app-bar
      app
      color="blue darken-3"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="oasaLogo.png"
          transition="scale-transition"
          width="40"
        />


      </div>

      <v-spacer>ok</v-spacer>


    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
