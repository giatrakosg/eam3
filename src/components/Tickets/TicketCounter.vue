<template lang="html">
  <v-card>
      <v-card-title>{{$t('text.ticketNum')}}</v-card-title>
      <v-card-text>
          <v-btn @click="subtract()">
            <v-icon>mdi-minus-box</v-icon>
          </v-btn>
          <v-text-field
            v-model="amount"
          >
          </v-text-field>
          <v-btn @click="add()">
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
    } ,
    methods : {
        subtract() {
            if (this.amount > 0) {
                this.amount = this.amount - 1;
                this.$store.dispatch('setAmount',this.amount);
            }
        } ,
        add() {
            this.amount = this.amount + 1;
            this.$store.dispatch('setAmount',this.amount);
        }
    }

}
</script>

<style lang="css" scoped>
</style>
