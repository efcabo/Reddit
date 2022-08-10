from datetime import datetime
from DB.connect import database_connect
from models import *


def insert_subreddit(subreddit):
    """
    Inserta ou actualiza un subreddit na BD.

    Parameters
    ----------
    subreddit :
        Subreddit para realizar a extracción

    """
    session = database_connect()

    result = session.query(Subreddit).filter(Subreddit.subreddit_id == subreddit.id)
    date = datetime.utcfromtimestamp(subreddit.created_utc).strftime('%Y-%m-%d %H:%M:%S')

    # Comproba se existe para insertalo ou actualizalo
    if result.count() == 0:

        to_insert = Subreddit(

            subreddit_id=subreddit.id,
            name=subreddit.name,
            display_name=subreddit.display_name,
            display_name_prefixed=subreddit.display_name_prefixed,
            title=subreddit.title,
            url=subreddit.url,
            created_utc=date,
            description=subreddit.description,
            description_html=subreddit.description_html,
            public_description=subreddit.public_description,
            public_description_html=subreddit.public_description_html,
            submit_text=subreddit.submit_text,
            submit_text_html=subreddit.submit_text_html,
            submit_text_label=subreddit.submit_text_label,
            accept_followers=subreddit.accept_followers,
            accounts_active=subreddit.accounts_active,
            accounts_active_is_fuzzed=subreddit.accounts_active_is_fuzzed,
            active_user_count=subreddit.active_user_count,
            all_original_content=subreddit.all_original_content,
            allow_discovery=subreddit.allow_discovery,
            allow_galleries=subreddit.allow_galleries,
            allow_images=subreddit.allow_images,
            allow_polls=subreddit.allow_polls,
            allow_prediction_contributors=subreddit.allow_prediction_contributors,
            allow_predictions=subreddit.allow_predictions,
            allow_predictions_tournament=subreddit.allow_predictions_tournament,
            allow_videogifs=subreddit.allow_videogifs,
            allow_videos=subreddit.allow_videos,
            can_assign_link_flair=subreddit.can_assign_link_flair,
            can_assign_user_flair=subreddit.can_assign_user_flair,
            collapse_deleted_comments=subreddit.collapse_deleted_comments,
            comment_score_hide_mins=subreddit.comment_score_hide_mins,
            community_icon=subreddit.community_icon,
            community_reviewed=subreddit.community_reviewed,
            disable_contributor_requests=subreddit.disable_contributor_requests,
            free_form_reports=subreddit.free_form_reports,
            hide_ads=subreddit.hide_ads,
            icon_img=subreddit.icon_img,
            is_crosspostable_subreddit=subreddit.is_crosspostable_subreddit,
            is_enrolled_in_new_modmail=subreddit.is_enrolled_in_new_modmail,
            lang=subreddit.lang,
            link_flair_enabled=subreddit.link_flair_enabled,
            notification_level=subreddit.notification_level,
            original_content_tag_enabled=subreddit.original_content_tag_enabled,
            over18=subreddit.over18,
            prediction_leaderboard_entry_type=subreddit.prediction_leaderboard_entry_type,
            public_traffic=subreddit.public_traffic,
            quarantine=subreddit.quarantine,
            restrict_commenting=subreddit.restrict_commenting,
            restrict_posting=subreddit.restrict_posting,
            should_archive_posts=subreddit.should_archive_posts,
            show_media=subreddit.show_media,
            show_media_preview=subreddit.show_media_preview,
            spoilers_enabled=subreddit.spoilers_enabled,
            submission_type=subreddit.submission_type,
            submit_link_label=subreddit.submit_link_label,
            subreddit_type=subreddit.subreddit_type,
            subscribers=subreddit.subscribers,
            suggested_comment_sort=subreddit.suggested_comment_sort,
            whitelist_status=subreddit.whitelist_status,
            wiki_enabled=subreddit.wiki_enabled,
            wls=subreddit.wls

        )

        session.add(to_insert)
        session.commit()

    else:

        result.display_name = subreddit.display_name
        result.display_name_prefixed = subreddit.display_name_prefixed
        result.title = subreddit.title
        result.url = subreddit.url
        result.created_utc = date
        result.description = subreddit.description
        result.description_html = subreddit.description_html
        result.public_description = subreddit.public_description
        result.public_description_html = subreddit.public_description_html
        result.submit_text = subreddit.submit_text
        result.submit_text_html = subreddit.submit_text_html
        result.submit_text_label = subreddit.submit_text_label
        result.accept_followers = subreddit.accept_followers
        result.accounts_active = subreddit.accounts_active
        result.accounts_active_is_fuzzed = subreddit.accounts_active_is_fuzzed
        result.active_user_count = subreddit.active_user_count
        result.all_original_content = subreddit.all_original_content
        result.allow_discovery = subreddit.allow_discovery
        result.allow_galleries = subreddit.allow_galleries
        result.allow_images = subreddit.allow_images
        result.allow_polls = subreddit.allow_polls
        result.allow_prediction_contributors = subreddit.allow_prediction_contributors
        result.allow_predictions = subreddit.allow_predictions
        result.allow_predictions_tournament = subreddit.allow_predictions_tournament
        result.allow_videogifs = subreddit.allow_videogifs
        result.allow_videos = subreddit.allow_videos
        result.can_assign_link_flair = subreddit.can_assign_link_flair
        result.can_assign_user_flair = subreddit.can_assign_user_flair
        result.collapse_deleted_comments = subreddit.collapse_deleted_comments
        result.comment_score_hide_mins = subreddit.comment_score_hide_mins
        result.community_icon = subreddit.community_icon
        result.community_reviewed = subreddit.community_reviewed
        result.disable_contributor_requests = subreddit.disable_contributor_requests
        result.free_form_reports = subreddit.free_form_reports
        result.hide_ads = subreddit.hide_ads
        result.icon_img = subreddit.icon_img
        result.is_crosspostable_subreddit = subreddit.is_crosspostable_subreddit
        result.is_enrolled_in_new_modmail = subreddit.is_enrolled_in_new_modmail
        result.lang = subreddit.lang
        result.link_flair_enabled = subreddit.link_flair_enabled
        result.notification_level = subreddit.notification_level
        result.original_content_tag_enabled = subreddit.original_content_tag_enabled
        result.over18 = subreddit.over18
        result.prediction_leaderboard_entry_type = subreddit.prediction_leaderboard_entry_type
        result.public_traffic = subreddit.public_traffic
        result.quarantine = subreddit.quarantine
        result.restrict_commenting = subreddit.restrict_commenting
        result.restrict_posting = subreddit.restrict_posting
        result.should_archive_posts = subreddit.should_archive_posts
        result.show_media = subreddit.show_media
        result.show_media_preview = subreddit.show_media_preview
        result.spoilers_enabled = subreddit.spoilers_enabled
        result.submission_type = subreddit.submission_type
        result.submit_link_label = subreddit.submit_link_label
        result.subreddit_type = subreddit.subreddit_type
        result.subscribers = subreddit.subscribers
        result.suggested_comment_sort = subreddit.suggested_comment_sort
        result.whitelist_status = subreddit.whitelist_status
        result.wiki_enabled = subreddit.wiki_enabled
        result.wls = subreddit.wls

        session.commit()


def insert_author(author):
    """
    Inserta ou actualiza un usuario na BD.

    Parameters
    ----------
    author :
        Usuario para realizar a extracción

    """

    session = database_connect()

    result = session.query(User).filter(User.user_id == author.id)
    date = datetime.utcfromtimestamp(author.created_utc).strftime('%Y-%m-%d %H:%M:%S')

    # Comproba se existe para insertalo ou actualizalo
    if result.count() == 0:

        to_insert = User(

            user_id=author.id,
            name=author.name,
            created_utc=date,
            subreddit=author.subreddit,
            accept_chats=author.accept_chats,
            accept_followers=author.accept_followers,
            accept_pms=author.accept_pms,
            awardee_karma=author.awardee_karma,
            awarder_karma=author.awarder_karma,
            comment_karma=author.comment_karma,
            has_subscribed=author.has_subscribed,
            has_verified_email=author.has_verified_email,
            hide_from_robots=author.hide_from_robots,
            icon_img=author.icon_img,
            is_employee=author.is_employee,
            is_gold=author.is_gold,
            is_mod=author.is_mod,
            link_karma=author.link_karma,
            pref_show_snoovatar=author.pref_show_snoovatar,
            snoovatar_img=author.snoovatar_img,
            total_karma=author.total_karma,
            verified=author.verified
        )

        session.add(to_insert)
        session.commit()

    else:

        result.name = author.name
        result.created_utc = date
        result.subreddit = author.subreddit
        result.accept_chats = author.accept_chats
        result.accept_followers = author.accept_followers
        result.accept_pms = author.accept_pms
        result.awardee_karma = author.awardee_karma
        result.awarder_karma = author.awarder_karma
        result.comment_karma = author.comment_karma
        result.has_subscribed = author.has_subscribed
        result.has_verified_email = author.has_verified_email
        result.hide_from_robots = author.hide_from_robots
        result.icon_img = author.icon_img
        result.is_employee = author.is_employee
        result.is_gold = author.is_gold
        result.is_mod = author.is_mod
        result.link_karma = author.link_karma
        result.pref_show_snoovatar = author.pref_show_snoovatar
        result.snoovatar_img = author.snoovatar_img
        result.total_karma = author.total_karma
        result.verified = author.verified

        session.commit()


def insert_submission(submission, author_id, subreddit_id):
    """
    Inserta unha publicación na base de datos.

    Parameters
    ----------
    submission :
        Publicación a insertar.
    author_id :
        ID do autor da publicación.
    subreddit_id :
        ID do subrredit no que se realizou a publicación

    """

    session = database_connect()

    result = session.query(Post).filter(Post.name == submission.name)

    # Comproba se existe
    if result.count() == 0:

        date_created = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')

        # Comproba que existan os campos para evitar erros
        date_approved = None
        date_edited = None
        date_banned = None

        if submission.approved_at_utc != None:
            date_approved = datetime.utcfromtimestamp(submission.approved_at_utc).strftime('%Y-%m-%d %H:%M:%S')
        if submission.edited != None:
            date_edited = datetime.utcfromtimestamp(submission.edited).strftime('%Y-%m-%d %H:%M:%S')
        if submission.banned_at_utc != None:
            date_banned = datetime.utcfromtimestamp(submission.banned_at_utc).strftime('%Y-%m-%d %H:%M:%S')

        # Obtén as claves do usuario e o subreddit
        user_key = session.query(User).filter(User.user_id == author_id).first().user_key
        subreddit_key = session.query(Subreddit).filter(
            Subreddit.subreddit_id == subreddit_id).first().subreddit_key

        to_insert = Post(

            post_id=submission.id,
            user_key=user_key,
            user_id=author_id,
            subreddit_key=subreddit_key,
            subreddit_id=subreddit_id,
            link_title=submission.title,
            name=submission.name,
            body=submission.selftext,
            body_html=submission.selftext_html,
            created_utc=date_created,
            approved_at_utc=date_approved,
            approved_by=submission.approved_by,
            archived=submission.archived,
            banned_by=submission.banned_by,
            banned_at_utc=date_banned,
            can_gild=submission.can_gild,
            can_mod_post=submission.can_mod_post,
            distinguished=submission.distinguished,
            downs=submission.downs,
            edited=date_edited,
            gilded=submission.gilded,
            locked=submission.locked,
            mod_note=submission.mod_note,
            mod_reason_by=submission.mod_reason_by,
            mod_reason_title=submission.mod_reason_title,
            no_follow=submission.no_follow,
            num_reports=submission.num_reports,
            permalink=submission.permalink,
            removal_reason=submission.removal_reason,
            report_reasons=submission.report_reasons,
            score=submission.score,
            send_replies=submission.send_replies,
            stickied=submission.stickied,
            top_awarded_type=submission.top_awarded_type,
            total_awards_received=submission.total_awards_received,
            ups=submission.ups,
            link_allow_live_comments=submission.allow_live_comments,
            link_category=submission.category,
            link_clicked=submission.clicked,
            link_comment_limit=submission.comment_limit,
            link_comment_sort=submission.comment_sort,
            link_contest_mode=submission.contest_mode,
            link_content_categories=submission.content_categories,
            link_discussion_type=submission.discussion_type,
            link_domain=submission.domain,
            link_hidden=submission.hidden,
            link_hide_score=submission.hide_score,
            link_is_crosspostable=submission.is_crosspostable,
            link_is_meta=submission.is_meta,
            link_is_reddit_media_domain=submission.is_reddit_media_domain,
            link_is_robot_indexable=submission.is_robot_indexable,
            link_is_self=submission.is_self,
            link_is_video=submission.is_video,
            link_flair_text=submission.link_flair_text,
            link_flair_type=submission.link_flair_type,
            link_media_only=submission.media_only,
            link_num_crossposts=submission.num_crossposts,
            link_num_comments=submission.num_comments,
            link_num_duplicates=submission.num_duplicates,
            link_over_18=submission.over_18,
            link_parent_whitelist_status=submission.parent_whitelist_status,
            link_pinned=submission.pinned,
            link_pwls=submission.pwls,
            link_quarantine=submission.quarantine,
            link_removed_by=submission.removed_by,
            link_removed_by_category=submission.removed_by_category,
            link_spoiler=submission.spoiler,
            link_suggested_sort=submission.suggested_sort,
            link_upvote_ratio=submission.upvote_ratio,
            link_url=submission.url,
            link_view_count=submission.view_count,
            link_visited=submission.visited,
            link_whitelist_status=submission.whitelist_status,
            link_wls=submission.wls

        )

        session.add(to_insert)
        session.commit()

        # Obtén a información dos premios asociados
        submission_key = session.query(Post).filter(Post.name == submission.name).first().post_key

        for award in submission.all_awardings:
            insert_award(award, submission_key, submission.id)


def insert_comment(comment, author_id, subreddit_id):
    """
    Inserta un comentario na base de datos.

    Parameters
    ----------
    comment :
        Comentario a insertar.
    author_id :
        ID do autor da publicación.
    subreddit_id :
        ID do subrredit no que se realizou a publicación

    """
    session = database_connect()

    result = session.query(Post).filter(Post.name == comment.name)

    # Comproba se existe
    if result.count() == 0:

        parent = session.query(Post).filter(Post.name == comment.parent_id)

        if parent.count() == 1:

            # Obten a clave e id da publicación á que responde o comentario
            parent_key = parent.first().post_key
            parent_id = parent.first().post_id

            date_created = datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')

            # Comproba que existan os campos para evitar erros
            date_approved = None
            date_edited = None
            date_banned = None

            if comment.approved_at_utc != None:
                date_approved = datetime.utcfromtimestamp(comment.approved_at_utc).strftime('%Y-%m-%d %H:%M:%S')
            if comment.edited != None:
                date_edited = datetime.utcfromtimestamp(comment.edited).strftime('%Y-%m-%d %H:%M:%S')
            if comment.banned_at_utc != None:
                date_banned = datetime.utcfromtimestamp(comment.banned_at_utc).strftime('%Y-%m-%d %H:%M:%S')

            # Obtén as claves do usuario e o subreddit
            user_key = session.query(User).filter(User.user_id == author_id).first().user_key
            subreddit_key = session.query(Subreddit).filter(
                Subreddit.subreddit_id == subreddit_id).first().subreddit_key

            to_insert = Post(

                post_id=comment.id,
                user_key=user_key,
                user_id=author_id,
                subreddit_key=subreddit_key,
                subreddit_id=subreddit_id,
                parent_key=parent_key,
                parent_id=parent_id,
                name=comment.name,
                body=comment.body,
                body_html=comment.body_html,
                created_utc=date_created,
                approved_at_utc=date_approved,
                approved_by=comment.approved_by,
                archived=comment.archived,
                banned_by=comment.banned_by,
                banned_at_utc=date_banned,
                can_gild=comment.can_gild,
                can_mod_post=comment.can_mod_post,
                distinguished=comment.distinguished,
                downs=comment.downs,
                edited=date_edited,
                gilded=comment.gilded,
                locked=comment.locked,
                mod_note=comment.mod_note,
                mod_reason_by=comment.mod_reason_by,
                mod_reason_title=comment.mod_reason_title,
                no_follow=comment.no_follow,
                num_reports=comment.num_reports,
                permalink=comment.permalink,
                removal_reason=comment.removal_reason,
                report_reasons=comment.report_reasons,
                score=comment.score,
                send_replies=comment.send_replies,
                stickied=comment.stickied,
                top_awarded_type=comment.top_awarded_type,
                total_awards_received=comment.total_awards_received,
                ups=comment.ups,
                comment_collapsed=comment.collapsed,
                comment_collapsed_because_crowd_control=comment.collapsed_because_crowd_control,
                comment_collapsed_reason=comment.collapsed_reason,
                comment_collapsed_reason_code=comment.collapsed_reason_code,
                comment_type=comment.comment_type,
                comment_controversiality=comment.controversiality,
                comment_is_submitter=comment.is_submitter,
                comment_score_hidden=comment.score_hidden

            )

            session.add(to_insert)
            session.commit()

            # Obtén a información dos premios asociados
            comment_key = session.query(Post).filter(Post.name == comment.name).first().post_key

            for award in comment.all_awardings:
                insert_award(award, comment_key, comment.id)


def insert_award(award, post_key, post_id):
    """
    Inserta os premios asociados ás publicacións na base de datos.

    Parameters
    ----------
    award :
        Premio a insertar.
    post_key :
        Clave da publicación ou comentario.
    post_id :
        ID da publicación ou comentario.

    """

    session = database_connect()

    result = session.query(Award).filter(Award.award_id == award['id'])

    # Comproba se existen os campos para evitar erros
    start_date = None
    end_date = None

    if award['start_date'] != None:
        start_date = datetime.utcfromtimestamp(award['start_date']).strftime('%Y-%m-%d %H:%M:%S')
    if award['end_date'] != None:
        end_date = datetime.utcfromtimestamp(award['end_date']).strftime('%Y-%m-%d %H:%M:%S')

    # Comproba se existe o premio para insertalo ou actualizalo
    if result.count() == 0:

        to_insert = Award(

            award_id=award['id'],
            name=award['name'],
            description=award['description'],
            award_sub_type=award['award_sub_type'],
            award_type=award['award_type'],
            coin_price=award['coin_price'],
            coin_reward=award['coin_reward'],
            subreddit_coin_reward=award['subreddit_coin_reward'],
            start_date=start_date,
            end_date=end_date,
            icon_url=award['id']

        )

        session.add(to_insert)
        session.commit()

    else:

        result.name = award['name']
        result.description = award['description']
        result.award_sub_type = award['award_sub_type']
        result.award_type = award['award_type']
        result.coin_price = award['coin_price']
        result.coin_reward = award['coin_reward']
        result.subreddit_coin_reward = award['subreddit_coin_reward']
        result.start_date = start_date
        result.end_date = end_date
        result.icon_url = award['id']

    # Establece a relación entre premios e publicacións
    result = session.query(Post_has_Award).filter(
        Post_has_Award.award_id == award['id']).filter(Post_has_Award.post_key == post_key)

    if result.count() == 0:
        award_key = session.query(Award).filter(Award.award_id == award['id']).first().award_key

        to_insert = Post_has_Award(

            award_key=award_key,
            award_id=award['id'],
            post_key=post_key,
            post_id=post_id

        )

        session.add(to_insert)
        session.commit()
