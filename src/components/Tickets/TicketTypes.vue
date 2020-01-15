<template lang="html">
    <div >
        <v-card>
            <v-card-title>{{$t('text.products')}}</v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <v-form name="simple" >
                    <v-radio-group v-model="product" :mandatory="false">
                        <v-radio label="1 εισητήριο 90 λεπτών" ></v-radio>
                        <v-radio label="5 εισητήρια 90 λεπτών" ></v-radio>
                        <v-radio label="10+1 εισητήρια 90 λεπτών" ></v-radio>
                        <v-radio label="1 ημέρας" ></v-radio>
                        <v-radio label="5 ημέρων" ></v-radio>
                        <v-radio label="30 ημέρων" ></v-radio>
                </v-radio-group>
                    <v-btn color="success" class="mr-4" @click.stop.prevent="submit()">Submit</v-btn>
                </v-form>
            </v-card-text>
        </v-card>
        <!--
        <v-select v-model="cardType" :items="cardTypes" label="Επιλέξτε τύπο προϊόντος" @change="HandleCardChange(cardTypes)"></v-select>
        -->
    </div>
</template>

<script>
export default {
    name : 'TicketTypes' ,
    data () {
        return {
            product : ''
        }
    }
}
</script>

<style lang="css" scoped>
</style>
