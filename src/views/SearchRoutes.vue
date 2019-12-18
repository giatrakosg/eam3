<template>

    <v-container fluid >
        <v-row >
            <v-col >
                <h2 style="color: #004B84;"> Journey Results</h2>
            </v-col>
        </v-row>
        <v-row dense>
            <v-col>
                <v-expansion-panels>
                <v-expansion-panel >
                    <v-expansion-panel-header >
                        <div class="font-weight-medium">Edit Preferences</div>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content >

                        <v-row>
                            <v-col cols="5">
                                 <SearchRoutesResultsForm />
                            </v-col>
                            <v-col cols="7">
                                <SearchRoutesResultsOptions/>
                            </v-col>
                        </v-row>
                        <v-row dense >
                            <v-col>
                                <v-btn class="my-2" color="success"  x-large >
                                    APPLY
                                </v-btn>
                            </v-col>

                        </v-row>

                    </v-expansion-panel-content>

                </v-expansion-panel>
                </v-expansion-panels>
            </v-col>
        </v-row>


    </v-container>


</template>

<script>
    import SearchRoutesResultsForm from "../components/SearchRoutes/SearchRoutesResultsForm";
    import SearchRoutesResultsOptions from "../components/SearchRoutes/SearchRoutesResultsOptions";
    export default {
        name: "SearchRoutes",
        components: {SearchRoutesResultsOptions, SearchRoutesResultsForm}
    }
</script>

<style scoped>

</style>