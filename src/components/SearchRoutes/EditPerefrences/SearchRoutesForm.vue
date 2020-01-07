<template>


        <v-card   color="#FAFAFA" elevation="0">

            <v-container  fluid >
                <v-row dense align="center">
                    <v-col cols="4">
                <span class="font-weight-light">
                    {{$t('text.from')}}:
                </span>
                    </v-col>
                    <v-col >
                        <v-text-field
                                class="font-weight-medium"
                                required
                                value="Here"
                        />
                    </v-col>

                </v-row>
                <v-row dense align="center">
                    <v-col cols="4">
                <span class="font-weight-light">
                    {{$t('text.to')}}:
                </span>
                    </v-col>
                    <v-col >
                        <v-text-field
                                class="font-weight-medium"
                                required
                                value="There"
                        />
                    </v-col>
                </v-row>
                <v-row dense align="center">
                    <v-col cols="4">
                        <span class="font-weight-light">
                            {{$t('text.leaving')}}:
                        </span>
                    </v-col >
                    <v-col class="font-weight-medium" >
                        <DateTime/>

                    </v-col>

                </v-row>

            </v-container>

        </v-card>


</template>

<script>
    import DateTime from "../../DateTime/DateTime";
    export default {
        name: "SearchRoutesForm",
        components:{DateTime}


    }
</script>

<style scoped>

</style>