<template lang="html">
  <v-container>
    <h1>Προϊόντα προς αγορά</h1>
    {{cardType}} x {{amount}}
    <br>
    Κόστος: {{calculate_cost(product, amount)}} €
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
  data:()=>({
        product: sessionStorage.getItem("product"),
        cardType: sessionStorage.getItem("cardType"),
        amount: sessionStorage.getItem("amount"),
    }),
    methods:{
        calculate_cost(a,b){
            switch(a){
                case "one":
                    return 140*b/100
                case "five":
                    return 700*b/100
                case "ten":
                    return 1400*b/100
                case "day"
                    return 500*b/100
                case "five_days"
                    return 1000*b/100
            }
            return -1
        },
        submit(){
            //show message
            
            this.$router.push("../tickets");
        }
    }
}
</script>

<style lang="css" scoped>
</style>
