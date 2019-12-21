<template>
    <v-col>
        <v-expansion-panels>
            <v-expansion-panel >
                <v-expansion-panel-header >
                    <div class="font-weight-medium">Edit Preferences</div>
                </v-expansion-panel-header>
                <v-expansion-panel-content >

                    <v-row>
                        <v-col cols="5">
                            <SearchRoutesForm />
                        </v-col>
                        <v-col cols="7">
                            <SearchRoutesOptions/>
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
</template>

<script>
    import SearchRoutesOptions from "./SearchRoutesOptions";
    import SearchRoutesForm from "./SearchRoutesForm";

    export default {
        name: "SearchRoutesEditPreferences",
        components: {SearchRoutesOptions, SearchRoutesForm}
    }
</script>

<style scoped>

</style>