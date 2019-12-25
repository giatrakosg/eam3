<template>
  <div >
    <v-row justify="center" dense>
      <v-col >
        <v-img  contain
                     src="../assets/athena-card.png">
        <SearchRouteForm class="m-5"/>
        </v-img>
      </v-col>
    </v-row>
    <v-layout row>
      <v-flex sm1 md1 lg1>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex sm4 md4 lg4>
        <Traffic />

      </v-flex>
    </v-layout>
    <v-row>
      <v-col>
      </v-col>
    </v-row>
  </div>
</template>

<script>


import SearchRouteForm from "../components/Home/HomeSearchRouteForm";
import Traffic from "../components/StationInfo/Traffic"
export default {
  name: 'Home',
  components: {
    SearchRouteForm ,
    Traffic
  },
};
</script>
