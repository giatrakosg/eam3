<template>
    <v-card
            max-width="400"
            color="#FAFAFA"
            elevation="10"

    >
        <v-card-title style="background:#1565C0 ">
            <span style="color: aliceblue">Where To Next?</span>
        </v-card-title>
        <v-form>
            <v-container >
                <v-row justify="center" dense>
                    <v-col>
                        <v-text-field
                                label="FROM"
                                required
                                v-model="from"
                        />
                    </v-col>
                    <v-spacer/>
                </v-row>
                <v-row justify="center" dense>
                    <v-col>
                        <v-text-field
                                label="TO"
                                required
                                v-model="to"
                        />
                    </v-col>
                    <v-col >
                        <v-btn text  width="100%" to="SearchRoutes"  style="text-decoration: none">
                            <i  class="fas fa-arrow-right fa-2x" style="color: #1565C0;"/>
                        </v-btn>

                    </v-col>

                </v-row>
                <DateTime v-on:childToParentTime="onChildClickTime" v-on:childToParentDate="onChildClickDate"/>

            </v-container>
        </v-form>
    </v-card>

</template>

<script>
    import DateTime from "../DateTime/DateTime";
    export default {
        name: "HomeSearchRouteForm",
        components: {DateTime},
        data: () => ({
            to:null,
            from:null,
            date:null,
            time:null

        }),
        methods:{
            onChildClickTime(value){
                this.time=value;
            },
            onChildClickDate(value){
                this.date=value;
            }
        }
    }
</script>

<style scoped>

</style>
