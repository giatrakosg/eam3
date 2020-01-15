<template lang="html">
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
      <div class="my-2">
        <v-btn href="/tickets/buy" depressed large>Αγορα απροσωπων εισητηριων</v-btn>
      </div>
      <div class="my-2">
        <v-btn href="/tickets/recharge" depressed large>Αγορα προσωποποιημενης καρτας ATH.ENA card</v-btn>
      </div>
      <div class="my-2">
        tooltip: Οι δικαιούχοι μειωμένου κόμιστρου πρέπει να εκδόσουν προσωποποιημένη κάρτα για να οφεληθούν από το μειωμένο κόμιστρα. Το σύστημα μέσω του ΑΜΚΑ θα μειώσει τις τιμές των προϊόντων αυτόματα.
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
