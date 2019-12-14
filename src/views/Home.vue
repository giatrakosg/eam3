<template>
  <v-row>

    <v-col class="m-2" >
      <v-parallax  height="500"
                   src="../../public/oasa2.jpg">


      <SearchRouteForm class="m-5"/>
      </v-parallax>

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
