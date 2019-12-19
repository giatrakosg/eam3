<template>

    <v-container fluid >
        <v-row >
            <v-col >
                <h2 style="color: #004B84;"> Journey Results</h2>
            </v-col>
        </v-row>
        <v-row dense>
            <SearchRoutesEditPreferences/>
        </v-row>


    </v-container>


</template>

<script>

    import SearchRoutesEditPreferences from "../components/SearchRoutes/SearchRoutesEditPreferences";
    export default {
        name: "SearchRoutes",
        components: {SearchRoutesEditPreferences}
    }
</script>

<style scoped>

</style>