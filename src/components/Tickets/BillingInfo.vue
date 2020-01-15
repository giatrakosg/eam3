<template lang="html">
    <div class="">
        <v-card>
            <v-card-title>
                {{$t('text.billing')}}
            </v-card-title>
            <v-card-text>
                <v-form name="persona" v-model="valid">
                    <v-text-field
                        v-model="user.first_name"
                        :rules="nameRules"
                        :counter="60"
                        label="First name"
                        required
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="user.last_name"
                        :rules="nameRules"
                        :counter="60"
                        label="Last name"
                        required
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="user.address"
                        :rules="nameRules"
                        :counter="90"
                        label="Address"
                        required
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="user.email"
                        :rules="emailRules"
                        :counter="90"
                        label="E-Mail"
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="pin"
                        :rules="numberRules"
                        :counter="8"
                        label="PIN"
                        required
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="AMKA"
                        :rules="numberRules"
                        :counter="11"
                        label="AMKA"
                        required
                        :disabled="isUser"
                    >
                    </v-text-field>
                    <v-btn block color="success" @click="submit()">
                        Αγορα
                    </v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </div>

</template>

<script>
export default {
    name : 'BillingInfo' ,
    data () {
        return {
            cardType : ''
        }
    } ,
    computed : {
        user() {
            return this.$store.state.user ;
        } ,
        isUser() {
            if (Object.keys(this.user).length == 0) {
                return false ;
            }
            else {
                return true ;
            }
        }
    } ,
    methods : {
        submit() {
            this.$router.push('/buysuccess')
        }
    }
}
</script>

<style lang="css" scoped>
</style>
