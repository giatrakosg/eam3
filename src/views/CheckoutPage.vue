<template lang="html">
  <v-container>
    <h1>Προϊόντα προς αγορά</h1>
    {{cardType}} x {{amount}}
    <br>
    Κόστος: {{calculate_cost(amount , cardType)}} €
    <br>
    <v-form name="persona" v-model="valid">
            <v-text-field v-model="firstname" :rules="nameRules" :counter="60" label="First name" required>
            </v-text-field>
            <v-text-field v-model="lastname" :rules="nameRules" :counter="60" label="Last name" required>
            </v-text-field>
            <v-text-field v-model="realaddress" :rules="adressRules" :counter="90" label="Address" required>
            </v-text-field>
            <v-text-field v-model="email" :rules="emailRules" :counter="90" label="E-Mail" required>
            </v-text-field>
            <v-text-field v-model="phone" :rules="phoneRules" :counter="13" label="Phone" required>
            </v-text-field>
            <v-btn
                @click="submit()"
                >Submit</v-btn>
        </v-form>
  </v-container>
</template>
<script>
export default {
    name : 'CheckoutPage' ,
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
        }

    }
}
</script>

<style lang="css" scoped>
</style>
