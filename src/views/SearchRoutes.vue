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