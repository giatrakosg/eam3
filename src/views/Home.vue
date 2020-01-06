<template>
  <div>
  <v-container >
    <v-row justify="center" dense>
      <v-col >
        <v-img contain
                     src="../assets/athena-card.png">
        <SearchRouteForm class="m-5"/>
        </v-img>
      </v-col>
    </v-row>
    <v-layout row>

      <v-flex sm4 md4 lg4>
        <Traffic />

      </v-flex>
    </v-layout>

  </v-container>
    <Footer />
  </div>
</template>

<script>


import SearchRouteForm from "../components/Home/HomeSearchRouteForm";
import Traffic from "../components/StationInfo/Traffic"
import Footer from "../components/Home/Footer";
export default {
  name: 'Home',
  components: {
    Footer,
    SearchRouteForm ,
    Traffic
  },
};
</script>
