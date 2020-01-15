<template lang="html">
  <v-card>
      <v-card-title>{{$t('text.ticketNum')}}</v-card-title>
      <v-card-text>
          <v-btn @click="amount = amount - 1">
            <v-icon>mdi-minus-box</v-icon>
          </v-btn>
          <v-text-field
            v-model="amount"
          >
          </v-text-field>
          <v-btn @click="amount = amount + 1">
            <v-icon>mdi-plus-box</v-icon>
          </v-btn>
      </v-card-text>
  </v-card>
</template>

<script>
export default {
    name : 'TicketCounter' ,
    data() {
        return {
            amount : 0
        }
    }
}
</script>

<style lang="css" scoped>
</style>
