<template>
  <v-app>
      <AppBar/>
    <v-content style="background-color:#BBE5F5 ">
      <v-layout>
        <v-flex xs1 md1 lg1>
          <v-spacer></v-spacer>
        </v-flex>
        <v-flex xs11 md11 lg11>
          <Breadcrumb />
        </v-flex>

      </v-layout>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>


import AppBar from "./components/AppBar/AppBar";
import Breadcrumb from "./components/Breadcrumb/Breadcrumb"
export default {
  name: 'App',
    components: {AppBar , Breadcrumb},
    data: () => ({
    //
  }),
};
</script>
