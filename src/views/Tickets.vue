<template lang="html">
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
      <div class="my-2">
        <v-btn href="/tickets/buy" depressed large>Buy Tickets As Guest</v-btn>
      </div>
      <div class="my-2">
        <v-btn href="/login" depressed large>Buy Tickets As User</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed large>ATH.ENA card</v-btn>
      </div>
      <div class="my-2">
        <v-btn href="/tickets/buy" depressed large color="Primary">Buy Tickets</v-btn>
      </div>
      <div class="my-2">
        <v-btn href="/tickets/reduced_info" depressed large color="Primary">Reduced</v-btn>
      </div>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name : 'Tickets'
}
</script>

<style lang="css" scoped>
</style>
