<template lang="html">
    <div >
        <v-card >
            <v-card-title>{{$t('text.successBuy')}} <v-icon>mdi-account-check</v-icon></v-card-title>
            <v-card-text>{{$t('text.thankyou')}}</v-card-text>
        </v-card>
    </div>
</template>

<script>
export default {
    name : 'SuccessBuyPage'
}
</script>

<style lang="css" scoped>
</style>
