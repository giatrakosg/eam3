<template lang="html">
  <v-container>
      <v-card class="my-4">
          <v-card-title>Προϊόντα προς αγορά</v-card-title>
          <v-card-subtitle>
              {{amount}} x {{typeName}}
          </v-card-subtitle>
          <v-card-subtitle>
              Κόστος: {{calculate_cost(amount , cardType)}} €
          </v-card-subtitle>
      </v-card>
    <BillingInfo />
  </v-container>
</template>
<script>
import BillingInfo from "../components/Tickets/BillingInfo"
export default {
    name : 'CheckoutPage' ,
    components : {BillingInfo},
    methods:{
        calculate_cost(a,b){
            switch(a){
                case 0:
                    return 140*b/100
                case 1:
                    return 700*b/100
                case 2:
                    return 1400*b/100
                case 3:
                    return 500*b/100
                case 4:
                    return 1000*b/100
            }
            return -1
        },
        submit(){
            //show message

            this.$router.push("../tickets");
        }
    } ,
    computed : {
        amount() {
            return this.$store.state.amount ;
        } ,
        cardType() {
            return this.$store.state.cardType ;
        } ,
        price() {
            return this.$store.state.price ;
        } ,
        typeName() {
            var type = "";
            switch (this.cardType) {
                case 0:
                    type = "1 εισητήριο 90 λεπτών" ;
                    break;
                case 1:
                    type = "5 εισητήρια 90 λεπτών" ;
                    break ;
                case 2:
                    type = "10+1 εισητήρια 90 λεπτών" ;
                    break ;
                case 3:
                    type = "1 ημέρας" ;
                    break ;
                case 4:
                    type = "5 ημέρων" ;
                    break ;
                case 5:
                    type = "30 ημέρων" ;
                    break ;
                default:

            }
            return type ;
        }

    }
}
</script>

<style lang="css" scoped>
</style>
