<template>
  <v-row justify="center" dense>

    <v-col >

      <v-img  contain
                   src="../../public/athena-card.png">
      <SearchRouteForm class="m-5"/>
      </v-img>


    </v-col>

  </v-row>
</template>

<script>


import SearchRouteForm from "../components/Home/SearchRouteForm";
export default {
  name: 'Home',
  components: {SearchRouteForm},
};
</script>
