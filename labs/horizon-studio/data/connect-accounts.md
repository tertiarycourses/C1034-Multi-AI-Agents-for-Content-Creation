# Connect your accounts (Labs 10-12) — optional, about 20 minutes

Every lab works in **dry-run** mode without this. Connect only accounts you
own, and only test pages and channels. Tokens go in .env — never in a prompt.

## LinkedIn (your own profile)
1. linkedin.com/developers -> Create app (needs a LinkedIn Page; a test page
   is fine).
2. Products -> add **Share on LinkedIn** and **Sign In with LinkedIn using
   OpenID Connect**.
3. Auth -> OAuth 2.0 tools -> create a token with scopes openid, profile,
   w_member_social. Paste it after LINKEDIN_ACCESS_TOKEN= in .env and save.
4. Your author ID: ask the agent "Look up my LinkedIn author ID with the
   token in .env and fill it in. Do not show me the token."
5. Leave LINKEDIN_VERSION as it is.

## Facebook Page
1. Create a test Facebook Page you manage.
2. developers.facebook.com -> Create app -> Business.
3. Graph API Explorer -> pick the app -> permissions pages_manage_posts,
   pages_read_engagement and pages_show_list -> Generate token -> choose
   your Page.
4. Click "Get Page Access Token"; paste it after FB_PAGE_TOKEN= in .env,
   and your Page ID (Page -> About -> Page transparency) after FB_PAGE_ID=.
   The key lasts about an hour, so make it just before you post.

## YouTube
1. console.cloud.google.com -> new project -> enable YouTube Data API v3.
2. OAuth consent screen: External, add yourself as a test user.
3. Credentials -> OAuth client ID -> Desktop app. Copy id and secret.
4. Ask the agent: "Help me sign in to YouTube once and save the refresh
   token in .env as YOUTUBE_REFRESH_TOKEN. Do not show me the token."
5. Uploads stay **private** until you make them public in YouTube Studio.
