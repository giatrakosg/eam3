<template>
  <v-app>
    <AppBar/>
    <v-content style="background-color:#BBE5F5 ">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>


import AppBar from "./components/AppBar/AppBar";
export default {
  name: 'App',
    components: {AppBar},
    data: () => ({
    //
  }),
};
</script>
