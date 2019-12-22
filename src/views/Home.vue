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
    <v-row>
      <v-col>
        <Traffic />
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
