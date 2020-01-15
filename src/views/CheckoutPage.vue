<template lang="html">
  <v-container>
    <h1>Προϊόντα προς αγορά</h1>
    {{cardType}} x 1
    <br>
    Κόστος: {{calculate_cost(product)}} €
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
    }),
    methods:{
        calculate_cost(a){
            switch(a){
                case "one":
                    return 1.40
                case "five":
                    return 7.00
                case "ten":
                    return 14.00
                
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
