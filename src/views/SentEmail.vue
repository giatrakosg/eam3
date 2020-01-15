<template lang="html">
    <div >
        <v-card>
            <v-card-title>
                {{$t('text.emailSucess')}}
                <v-icon>
                    mdi-account-check
                </v-icon>
            </v-card-title>
        </v-card>
    </div>
</template>

<script>
export default {
    name : 'SentEmail'
}
</script>

<style lang="css" scoped>
</style>
