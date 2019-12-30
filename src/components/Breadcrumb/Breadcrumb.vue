<template>
  <div>
    <v-breadcrumbs :items="this.GetCrumbs()" divider=">"/>
  </div>
</template>

<script>
  export default {
    name : 'Breadcrumb' ,
    data: () => ({

    }),
    methods:{
      GetCrumbs(){

        let info,k;
        let breadcrumbs_array=[
          {
            text: 'Home',
            disabled: false,
            href: '/',
          }

        ];

        info=this.$route.matched;

        for ( k in info ) {
          if (info.hasOwnProperty(k)) {
            // eslint-disable-next-line no-console
            console.log(info[k])
            let path = info[k].path;
            if(path===""){continue;}

            let text = info[k].meta.breadCrumb;

            breadcrumbs_array.push({
              text: text,
              disabled: false,
              href: path
            })
          }
        }

        return breadcrumbs_array;
      }
    }
  }
</script>

<style lang="css" scoped>
</style>
