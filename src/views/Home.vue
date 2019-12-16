<template>
  <v-row justify="start">

    <v-col class="m-2" >
      <v-img  contain  position="left"
                   src="../../public/eisitiria1217sk.png">


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
