<template lang="html">
  <v-card>
      <v-card-title>{{$t('text.ticketNum')}}</v-card-title>
      <v-card-text>
          <v-text-field
            v-model="amount"
            type="number"
            :rules="rules"
            @change="submit()"
          >
          </v-text-field>
      </v-card-text>
  </v-card>
</template>

<script>
export default {
    name : 'TicketCounter' ,
    data() {
        return {
            amount : 0 ,
            rules: [
                 v => !!v || 'Required',
                 v => v >= 0 || 'Incorrect',
                 v => v <= 100 || 'Max 100 tickets',
            ],

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
        },
        submit()  {
            this.$store.dispatch('setAmount',this.amount);            
        }
    }

}
</script>

<style lang="css" scoped>
</style>
