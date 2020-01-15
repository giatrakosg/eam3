<template>

    <v-container fluid >
        <v-row >
            <v-col >
                <h2 style="color: #004B84;"> {{$t('text.journeyresults')}}</h2>
            </v-col>
        </v-row>
        <v-row dense>
            <SearchRoutesEditPreferences/>
        </v-row>


        <v-row >
            <v-col>
            <v-card>
            <SearchRoutesDirections/>
            </v-card>
            </v-col>
        </v-row>
        <v-row >
            <v-col cols="auto">
                <v-card>
                    <v-card-text>
                        <span style="color: #004B84;">
                        TICKET PRICE:
                        </span>
                        <span class="ml-3" style="font-weight: bolder;color: black">
                            1,4
                             <i class="fas fa-euro-sign"></i>

                            <span style="font-size: small;color: #004B84" class="ml-2" >  90min</span>
                            <a class="ml-4" href="/tickets" > {{$t('text.tickets')}}</a>
                        </span>


                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>



    </v-container>


</template>

<script>

    import SearchRoutesEditPreferences from "../components/SearchRoutes/EditPerefrences/SearchRoutesEditPreferences";
    import SearchRoutesDirections from "../components/SearchRoutes/SearchRoutesResults/SearchRoutesDirections";
    export default {
        name: "SearchRoutes",
        components: {SearchRoutesDirections, SearchRoutesEditPreferences}
    }
</script>

<style scoped>

</style>