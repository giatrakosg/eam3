<template>
  <v-row justify="center" dense>

    <v-col >

      <v-img  contain
                   src="../assets/athena-card.png">
      <SearchRouteForm class="m-5"/>
      </v-img>


    </v-col>

  </v-row>
</template>

<script>


import SearchRouteForm from "../components/Home/HomeSearchRouteForm";
export default {
  name: 'Home',
  components: {SearchRouteForm},
};
</script>
