<template lang="html">
  <v-row align="center">
    <v-layout row wrap>
        <v-flex xs0 sm0 md1 lg1></v-flex>
        <v-flex xs12 sm12 md10 lg10>
            <v-card>
                <v-card-title class="justify-center">
                  <v-img
                    src="https://www.newmoney.gr/wp-content/uploads/2019/07/mhxannn-550x289.jpg"
                    height="200"
                    gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
                    >
                  </v-img>
                </v-card-title >
                <v-card-text>
                   <v-tooltip bottom>
                       <template v-slot:activator="{ on }">
                           <v-layout row wrap>
                               <v-flex xs0 sm0 md1 lg1>
                                   <v-spacer></v-spacer>
                               </v-flex>
                               <v-flex xs12 sm12 md4 lg4>
                                   <v-btn v-on="on" to="/tickets/buy" block color="success">{{$t("text.buy_tickets")}}</v-btn>
                               </v-flex>
                               <v-flex xs0 sm0 md1 lg1>
                                   <v-spacer></v-spacer>
                               </v-flex>
                               <v-flex xs12 sm12 md4 lg4 wrap>
                                   <v-btn v-on="on" to="/tickets/recharge" block color="success">{{$t("text.buy_personalizedcard")}}</v-btn>
                               </v-flex>
                               <v-flex xs0 sm0 md1 lg1>
                                   <v-spacer></v-spacer>
                               </v-flex>
                           </v-layout>
                      </template>
                      <span> Οι δικαιούχοι μειωμένου κόμιστρου πρέπει να εκδόσουν προσωποποιημένη κάρτα για να οφεληθούν από το μειωμένο κόμιστρα. <br/> Το σύστημα μέσω του ΑΜΚΑ θα μειώσει τις τιμές των προϊόντων αυτόματα.</span>
                  </v-tooltip >
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
  </v-row>
</template>
<script>
export default {
  name : 'Tickets'
}
</script>

<style lang="css" scoped>
</style>
