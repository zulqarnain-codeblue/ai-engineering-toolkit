# Pack: Shopify Themes and Storefronts

Use for Shopify themes; use a separate app pack for Shopify apps.

## Inspect
- Theme structure, Liquid sections/snippets/templates, JSON templates, settings schema, assets, locale files, and package scripts.
- Check Shopify requirements and the store's current theme architecture.
- Preserve merchant configurability and existing storefront behavior.

## Standards
- Use semantic Liquid and accessible HTML.
- Keep section settings validated and sensible.
- Avoid unnecessary JavaScript and layout shifts.
- Test product variants, availability, cart interactions, responsive states, localization, and empty/error states where relevant.
- Keep storefront API tokens and private app credentials out of theme code.
- Do not assume checkout can be modified beyond Shopify's supported extension points.

## Suggested tools
- Shopify CLI: https://github.com/Shopify/cli
- Theme Check: https://github.com/Shopify/theme-check
- Playwright: https://github.com/microsoft/playwright

## Verification
Run Theme Check and available build/lint scripts; test preview storefront behavior at mobile and desktop sizes. Use test products and safe environments for purchase flows.
