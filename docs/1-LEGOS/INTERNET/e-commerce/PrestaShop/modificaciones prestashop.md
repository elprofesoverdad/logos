# modificaciones prestashop

All rights reserved


daniel@daniel-laptop:/var/www/html$ ag "All rights reserved" --color --group -C 2 tienda
tienda/admin572ymosckgdxufddv47/themes/default/template/controllers/login/content.tpl
172-            <p class="text-center text-muted">
173-                    <a href="https://www.prestashop.com/" onclick="return !window.open(this.href);">
174:                            &copy; PrestaShop&#8482; 2007-{$smarty.now|date_format:"%Y"} - All rights reserved
175-                    </a>
176-            </p>


imagenes en admin:///var/www/html/tienda/img/

y

admin:///var/www/html/tienda/admin572ymosckgdxufddv47/themes/default/public/

y

admin:/var/www/html/tienda/admin572ymosckgdxufddv47/themes/default/img/

y en el admin lo que deje modificar es decir por bakend se pueden subir algunas imageness


renombrar los caches en admin:/var/www/html/tienda/var/cache/ el de dev desarrollo y prod produccion


modificar en layaout.tlp en /var/www/html/tienda/admin572ymosckgdxufddv47/themes/new-theme/template/

{* Logo *}
      <i class="material-icons js-mobile-menu">menu</i>
      <a id="header_logo" class="" href="{$default_tab_link|escape:'html':'UTF-8'}"><img src="{$img_dir}tu-logo.png" alt="Tu Tienda" /></a>
      <span id="shop_version">{$ps_version}</span>


y crear la imagen el /img de prestashop la imagen del logo tu-logo.png

en el siquiente eliminar prestashp y colocar mundo mejor
admin250umkiw5661yvx0xac/themes/default/template/controllers/login/header.tpl
40-             <meta name="robots" content="NOFOLLOW, NOINDEX">
41-             <title>
42:                     {$shop_name} {if $meta_title != ''}{if isset($navigationPipe)}{$navigationPipe|escape:'html':'UTF-8'}{else}&gt;{/if} {$meta_title}{/if} (PrestaShop&trade;)
43-             </title>


translations/es-ES/ShopThemeGlobal.es-ES.xlf
523-      <trans-unit id="7601c8e861088bd27255e18afaefab6b" approved="yes">
524-        <source>%copyright% %year% - Ecommerce software by %prestashop%</source>
525:        <target state="final">%copyright% %year% - Software Ecommerce desarrollado por %prestashop%</target>
526-        <note>Line: 41</note>
527-      </trans-unit>

translations/es-VE/ShopThemeGlobal.es-VE.xlf
523-      <trans-unit id="7601c8e861088bd27255e18afaefab6b" approved="yes">
524-        <source>%copyright% %year% - Ecommerce software by %prestashop%</source>
525:        <target state="final">%copyright% %year% - Software Ecommerce desarrollado por %prestashop%</target>
526-        <note>Line: 41</note>
527-      </trans-unit>


en admin:/var/www/html/themes/classic/templates/_partials/footer.tpl
hay que estar pendiente porque prestashop tiene variables de copyright que cambian de acuerdo al idioma


modificar el footer asi

    <div class="row">
      <div class="col-md-12">
        <p class="text-sm-center">
          {block name='copyright_link'}
            <a href="https://www.mundomejor.uk/" target="_blank" rel="noopener noreferrer nofollow">
              {l s='%copyright% %year% - Ecommerce software by %prestashop%' sprintf=['%prestashop%' => 'PrestaShop™', '%year%' => 'Y'|date, '%copyright%' => '©'] d='Shop.Theme.Global'}
            </a>
          {/block}
        </p>
      </div>
    </div>
  </div>
</div>

para eliminar el boton de ayuda para los que no son administradores

cambiar admin:/var/www/html/admin250umkiw5661yvx0xac/themes/new-theme/template/page_header_toolbar.tpl


buscar

           {if isset($help_link) and $help_link != false}

              {if $enableSidebar}
                <a class="btn btn-outline-secondary btn-help btn-sidebar" href="#"
                   title="{l s='Help' d='Admin.Global'}"
                   data-toggle="sidebar"
                   data-target="#right-sidebar"
                   data-url="{$help_link|escape}"
                   id="product_form_open_help"
                >
                  {l s='Help' d='Admin.Global'}
                </a>
              {else}
                <a class="btn btn-outline-secondary btn-help" href="{$help_link|escape}" title="{l s='Help' d='Admin.Global'}">
                  {l s='Help' d='Admin.Global'}

cambiar

           {if isset($help_link) and $help_link != false}


por

            {if isset($help_link) and $help_link == false}


