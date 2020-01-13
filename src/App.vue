<template>
  <v-app>


      <AppBar  />
    <v-content style="background-color:#BBE5F5 ">
      <v-container fluid>
        <Breadcrumb class="ml-7" />
        <router-view/>
      </v-container>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>


import AppBar from "./components/AppBar/AppBar";
import Breadcrumb from "./components/Breadcrumb/Breadcrumb"
import Footer from "./views/Footer";
export default {
  name: 'App',
    components: { Footer, AppBar , Breadcrumb},
    data: () => ({

    })

};
</script>
